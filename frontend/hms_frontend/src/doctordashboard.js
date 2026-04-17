import React, { useState } from "react";
import API from "./api";

function DoctorDashboard({ user }) {
  const [slot, setSlot] = useState({
    date: "",
    start_time: "",
    end_time: "",
  });

  const createSlot = async () => {
    try {
      await API.post("create-slot/", {
        ...slot,
        doctor_id: user.user_id,
      });
      alert("Slot created");
      setSlot({ date: "", start_time: "", end_time: "" });
    } catch (err) {
      console.error(err);
      alert("Error creating slot");
    }
  };

  return (
    <div className="full-page doctor-bg">
      <div className="overlay">
        <div className="center-container bg-card">
          <h2 className="page-title">Doctor Dashboard</h2>

          <div className="form-row">
            <label>Date</label>
            <input
              type="date"
              className="form-input"
              value={slot.date}
              onChange={(e) => setSlot({ ...slot, date: e.target.value })}
            />
          </div>

          <div className="form-row">
            <label>Start Time</label>
            <input
              type="time"
              className="form-input"
              value={slot.start_time}
              onChange={(e) =>
                setSlot({ ...slot, start_time: e.target.value })
              }
            />
          </div>

          <div className="form-row">
            <label>End Time</label>
            <input
              type="time"
              className="form-input"
              value={slot.end_time}
              onChange={(e) => setSlot({ ...slot, end_time: e.target.value })}
            />
          </div>

          <button className="primary-btn mt-4" onClick={createSlot}>
            Create Slot
          </button>
        </div>
      </div>
    </div>
  );
}

export default DoctorDashboard;

import React, { useEffect, useState } from "react";
import API from "./api";
import emailjs from "emailjs-com";


function PatientDashboard({ user }) {

  const [slots, setSlots] = useState([]);

  // 🔹 FETCH SLOTS
  const getSlots = async () => {
    try {
      const res = await API.get("get-slot/");
      setSlots(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  // 🔹 EMAIL FUNCTION
  const SERVICE_ID = process.env.REACT_APP_EMAILJS_SERVICE_ID;
  const TEMPLATE_ID = process.env.REACT_APP_EMAILJS_TEMPLATE_ID;
  const PUBLIC_KEY = process.env.REACT_APP_EMAILJS_PUBLIC_KEY;

  const sendEmails = (slot, patientEmail, doctorEmail) => {
    const params = {
      date: slot.date,
      time: slot.start_time,
    };

    // Patient email
    emailjs.send(
      //SERVICE_ID,
      //TEMPLATE_ID,
      
      {
        ...params,
        to_email: patientEmail,
      },
      //PUBLIC_KEY
      
    );

    // Doctor email
    emailjs.send(
      
      "service_v7t7ucm",
      "template_ezm80u6",
      {
        ...params,
        to_email: doctorEmail,
      },
      //PUBLIC_KEY
      
    );
  };
  useEffect(() => {
    getSlots();
}, []);
  

 

  // 🔹 BOOK SLOT
  async function bookSlot(slot) {
    try {
      await API.post("book-slot/", {
        slot_id: slot.id,
        patient_id: user.user_id,
      });


      sendEmails(
        slot,
        user.email,
        "doctor@gmail.com"
      );


      //addToCalendar(slot);
      alert("Booked + Email + Calendar Added");

      getSlots();

    } catch (err) {
      console.error(err);
      alert("Error booking");
    }
  }

  return (
    <div className="full-page patient-bg">
      <div className="overlay">
        <div className="center-container bg-card">
          <h2 className="page-title">Patient Dashboard</h2>

          {slots.length === 0 && <p>No slots available.</p>}

          {slots.map((slot) => (
            <div key={slot.id} className="slot-card">
              <p>
                {slot.date} | {slot.start_time}
              </p>
              <button
                className="primary-btn"
                onClick={() => bookSlot(slot)}
              >
                Book
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default PatientDashboard;
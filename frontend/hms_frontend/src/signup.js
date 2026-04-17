import React, { useState } from "react";
import API from "./api";

function Signup({ setUser }) {
  const [data, setData] = useState({
    username: "",
    password: "",
    role: "doctor",
  });

  const handleSignup = async () => {
    try {
      await API.post("signup/", data);
      alert("Signup successful");
      window.location.reload();
    } catch (err) {
      console.error(err);
      alert("Signup failed");
    }
  };

  return (
    <div className="auth-inner">
      <h2 className="form-title">Signup</h2>

      <input
        className="form-input"
        placeholder="Username"
        onChange={(e) => setData({ ...data, username: e.target.value })}
      />

      <input
        type="password"
        className="form-input"
        placeholder="Password"
        onChange={(e) => setData({ ...data, password: e.target.value })}
      />

      <select
        className="form-input"
        onChange={(e) => setData({ ...data, role: e.target.value })}
      >
        <option value="doctor">Doctor</option>
        <option value="patient">Patient</option>
      </select>

      <button className="primary-btn mt-4" onClick={handleSignup}>
        Signup
      </button>
    </div>
  );
}

export default Signup;

import React, { useState } from 'react';
import Login from './login';
import Signup from './signup';
import DoctorDashboard from './doctordashboard';
import PatientDashboard from './patientdashboard';
import './App.css';  

function App() {
  const [page, setpage] = useState("login");
  const [user, setUser] = useState(null);

  console.log("App user state:", user);
  if (user) {
    return (
      <div
        className={
          user.role === "doctor"
            ? "full-page doctor-bg"
            : "full-page patient-bg"
        }
      >
        <div className="overlay">
          {user.role === "doctor" ? (
            <DoctorDashboard user={user} />
          ) : (
            <PatientDashboard user={user} />
          )}
        </div>
      </div>
    );
  }

  return (
    <div className="full-page hospital-bg">
      <div className="overlay">
        <div className="auth-card">
          <h1 className="main-title">Hospital Management</h1>

          {page === "login" ? (
            <Login setUser={setUser} />
          ) : (
            <Signup setUser={setUser} />
          )}

          <div className="switch-buttons">
            <button onClick={() => setpage("login")} className="switch-btn">
              Go Login
            </button>
            <button onClick={() => setpage("signup")} className="switch-btn">
              Go Signup
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

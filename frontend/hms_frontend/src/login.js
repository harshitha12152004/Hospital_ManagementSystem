import React, { useState } from "react";
import API from "./api";

function Login({ setUser }) {
  const [data, setData] = useState({
    username: "",
    password: "",
  });

  const handleLogin = async () => {
    try {
      const res = await API.post("login/", data);
      
      setUser(res.data);
    } catch (err) {
     
      alert("Login failed");
    }
  };

  return (
    <div className="auth-inner">
      <h2 className="form-title">Login</h2>

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

      <button className="primary-btn mt-4" onClick={handleLogin}>
        Login
      </button>
    </div>
  );
}

export default Login;

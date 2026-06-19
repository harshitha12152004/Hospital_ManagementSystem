HMS Frontend - React Patient & Doctor Dashboard

React.js frontend for Hospital Management System. Handles user auth, slot booking, and role-based dashboards.

**Live Demo**: https://hms-frontend-xyz.onrender.com

✨ Features

- **Patient Dashboard**: View available doctor slots, book appointments in 1 click
- **Doctor Dashboard**: Manage availability, view upcoming patient bookings
- **JWT Auth**: Login/Register with token storage + protected routes
- **Real-time Updates**: Fetches slots from `GET /get-slot/` and updates UI after booking
- **Responsive UI**: Mobile-friendly design using CSS3 + Bootstrap
- **Error Handling**: Loading states for Render cold starts, CORS error fallbacks

🛠️ Tech Stack

React.js, JavaScript ES6+, Axios, React Router, CSS3, HTML5, Render

🚀 Live Links

|  | URL |
| --- | --- |
| **Frontend** | https://hospital-managementsystem-1.onrender.com|
| **Backend API** | https://hospital-managementsystem.onrender.com |

**Demo Login**  
Patient: `patient@test.com` / `Test123!`

📂 Project Structure

frontend/hms_frontend/
├── public/
│   └── http://index.html
├── src/
│   ├── components/
│   │   ├── Auth/           # Login, Register forms
│   │   ├── Dashboard/      # Patient & Doctor dashboards
│   │   ├── Slots/          # SlotList, BookingButton
│   │   └── Common/         # Navbar, Loader
│   ├── services/
│   │   └── http://api.js          # Axios instance + API calls
│   ├── http://App.js
│   └── http://index.js
├── .env.example
└── http://package.json

🔧 Run Locally

```bash
cd frontend/hms_frontend
npm install
npm start
App runs at `http://localhost:3000`

📡 Key API Calls

All requests handled via `src/services/api.js` using Axios:
Action	Endpoint	Method
Login	`/api/login/`	`POST`
Get Slots	`/api/get-slot/`	`GET`
Book Slot	`/api/book-slot/`	`POST`
Get My Bookings	`/api/bookings/`	`GET`
JWT token stored in `localStorage` and sent as `Authorization: Bearer <token>`

🎨 Main Components

1. *Login.js* - Handles auth, stores JWT, redirects by role
2. *PatientDashboard.js* - Calls `GET /get-slot/`, renders slot cards
3. *SlotCard.js* - Displays date/time, `Book` button triggers `POST /book-slot/`
4. *DoctorDashboard.js* - Shows doctor's bookings + create slot form

🚀 Deployment

Deployed on Render as Static Site  
*Build Command*: `npm run build`  
*Publish Directory*: `build`  

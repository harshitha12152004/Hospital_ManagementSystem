Hospital Management System

[![Live Demo](https://img.shields.io/badge/Live-Demo-green?style=for-the-badge)](https://hospital-managementsystem-1.onrender.com)
[![Backend API](https://img.shields.io/badge/API-Render-blue?style=for-the-badge)](https://hospital-managementsystem.onrender.com)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-black?style=for-the-badge&logo=github)](https://github.com/harshitha12152004/Hospital_ManagementSystem)

Full-stack hospital portal for patients to book doctor appointments with automated Google Calendar events and email confirmations.

✨ Features

- **Patient Dashboard**: View real-time available slots, book appointments instantly
- **Doctor Dashboard**: Manage availability, view upcoming bookings  
- **Google Calendar Integration**: Auto-creates calendar events using Service Account on booking
- **Email Notifications**: Confirmation to patient + alert to doctor via Django `send_mail`
- **Role-Based Access**: Separate auth flows for Patient, Doctor, Admin using JWT
- **Secure Deployment**: `.env` and `credentials.json` excluded via `.gitignore`

🛠️ Tech Stack

**Frontend**: React.js, JavaScript, Axios, CSS3, HTML5  
**Backend**: Django REST Framework, Python  
**Database**: PostgreSQL  
**Integrations**: Google Calendar API, SMTP Email  
**Deployment**: Render  

🚀 Live Demo

|  | URL |
| --- | --- |
| **Frontend** | https://hospital-managementsystem-1.onrender.com |
| **Backend API** | https://hospital-managementsystem.onrender.com |

**Test Credentials**  
Patient Login: `patient@test.com` / `Test123!`

📸 Demo Flow

1. Login as patient → Dashboard shows available slots from `GET /get-slot/`
2. Click **Book** → `POST /book-slot/` creates booking 
3. Check email for confirmation + Google Calendar for auto-created event

📂 Project Structure

Hospital_ManagementSystem/
├── backend/                    # Django REST Framework
│   ├── hms_api/               # Main app: views, models, serializers
│   ├── google_calendar.py     # Service Account calendar integration
│   ├── http://requirements.txt
│   └── http://manage.py
├── frontend/hms_frontend/      # React patient/doctor dashboard
│   ├── src/components/
│   └── http://package.json
├── database/
│   └── http://schema.sql             # Full Supabase/PostgreSQL schema + RLS
└── .gitignore                 # Excludes .env, http://credentials.json

🔧 Run Locally

**1. Backend Setup**
```bash
cd backend
pip install -r requirements.txt
Create `.env` file:
SECRET_KEY=your_django_secret
DATABASE_URL=postgresql://user:pass@localhost:5432/hms
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
GOOGLE_CALENDAR_ID=your_calendar_id@group.calendar.google.com
Add `credentials.json` for Google Service Account to `/backend/`
python manage.py migrate
python manage.py runserver
*2. Frontend Setup*
cd frontend/hms_frontend
npm install
Create `.env` file:
REACT_APP_API_URL=http://localhost:8000
npm start
⚙️ How It Works

Booking Flow
1. *Frontend React*: Patient Dashboard calls `GET /get-slot/` to fetch available slots
2. *User Action*: Patient clicks "Book" → Frontend sends `POST /book-slot/` with `slot_id` + `patient_id`
3. *Backend Django*: 
   - Validates slot is not booked
   - Creates `Booking` record linking patient, doctor, slot
   - Marks slot `is_booked = True`
   - Sends confirmation email to patient + notification to doctor
   - Calls `create_event()` to add appointment to Google Calendar
4. *Response*: `{"msg": "Booked successfully"}` returned to frontend

Google Calendar Integration
- Uses Google Service Account + `credentials.json` key file
- Scope: `https://www.googleapis.com/auth/calendar`
- Calendar ID configured via `CALENDAR_ID` env var
- Event created with: Summary, description, start/end time in `Asia/Kolkata` timezone

Email Notifications  
Django `send_mail` sends:
- *To Patient*: Appointment confirmation with doctor, date, time
- *To Doctor*: New booking alert with patient details

🔒 Security

Repository uses `.gitignore` to prevent committing sensitive files:
.env
credentials.json
*.sqlite3
node_modules/
Only source code is pushed to GitHub. All secrets remain local or in Render environment variables.

📊 Database Schema

Located in `/database/schema.sql`. Key tables:
- `profiles` - Users with role: subscriber/admin
- `subscriptions` - Monthly/Yearly plans with Stripe IDs
- `scores` - Rolling 5 golf scores per user
- `availability_slots` - Doctor schedule
- `bookings` - Links patient + doctor + slot

Includes RLS policies for Supabase.

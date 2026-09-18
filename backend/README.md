 HMS Backend - Django REST Framework API

REST API for Hospital Management System handling authentication, appointments, and Google Calendar integration.

**Base URL**: https://hospital-managementsystem.onrender.com

🔑 Key Features
- JWT Authentication for Patient, Doctor, Admin roles
- Slot booking with conflict prevention
- Google Calendar API integration via Service Account
- SMTP email notifications on booking
- PostgreSQL database with Django ORM

🛠️ Tech Stack
Python, Django 4.x, Django REST Framework, PostgreSQL, Gunicorn, Render

📡 API Endpoints

| Method | Endpoint | Description | Auth |
| --- | --- | --- | --- |
| `POST` | `/api/register/` | Create new patient account | No |
| `POST` | `/api/login/` | Returns JWT access + refresh token | No |
| `GET` | `/api/get-slot/` | Fetch all available appointment slots | JWT |
| `POST` | `/api/book-slot/` | Book a slot: `{slot_id, patient_id}` | JWT |
| `GET` | `/api/bookings/` | Get bookings for logged-in user | JWT |
| `POST` | `/api/create-slot/` | Doctor creates availability | JWT Doctor |

🔧 Setup & Run Locally

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
API runs at `http://localhost:8000`

🔐 Google Calendar Setup

1. Create Service Account in Google Cloud Console
2. Enable Google Calendar API
3. Download `credentials.json` → place in `/backend/`
4. Share your target Google Calendar with service account email
5. Set `GOOGLE_CALENDAR_ID` in `.env`

🚀 Deployment

Deployed on Render as Web Service  
*Build Command*: `pip install -r requirements.txt`  
*Start Command*: `gunicorn hms_backend.wsgi:application`

📂 Project Structure
backend/
├── hms_backend/        # Settings, wsgi, urls
├── hms_api/           # App: models.py, views.py, serializers.py
├── google_calendar.py # Calendar event creation logic
├── requirements.txt
└── manage.py

## How It Works

### Overview

This project is a Hospital Management System with:
- **Backend:** Django REST Framework (`hms-back`)
- **Frontend:** React (`front/hmsfront`)
- **Integrations:** Email notifications and Google Calendar events

Patients can view available appointment slots and book a consultation with a doctor.  
When a booking is made, the system sends emails and creates a Google Calendar event.

---

### Booking Flow

#### 1. Frontend (React)

- The **Patient Dashboard** calls `GET /get-slot/` to fetch all available slots.
- Slots are displayed with date and time.
- When the user clicks **“Book”**:
  - The frontend sends a `POST /book-slot/` request with:
    - `slot_id`
    - `patient_id`
  - On success, the frontend shows a confirmation message to the user.

#### 2. Backend (Django REST)

The `book_slot` view handles the booking:

1. Fetches the requested `AvailabilitySlot`.
2. Checks if the slot is already booked.
3. Gets the `patient` and `doctor`.
4. Creates a `Booking` record linking patient, doctor, and slot.
5. Marks the slot as `is_booked = True` and saves it.
6. Sends emails:
   - Confirmation email to the patient.
   - Notification email to the doctor.
7. Calls `create_event(slot, patient, doctor)` to add the appointment to Google Calendar.

The response `{"msg": "Booked successfully"}` is returned to the frontend.

---

### Google Calendar Integration

- Implemented in `google_calendar.py`.
- Uses a **Google Service Account** and a `credentials.json` key file.
- Uses the Google Calendar API with the scope:
  - `https://www.googleapis.com/auth/calendar`
- The calendar to use is configured via `CALENDAR_ID`
  (a Google Calendar ID like `...@group.calendar.google.com`).

When `create_event(slot, patient, doctor)` is called:

1. Loads credentials from `credentials.json`.
2. Builds a Calendar API client.
3. Combines `slot.date` and `slot.start_time` / `slot.end_time` into `dateTime`.
4. Creates an event with:
   - Summary: `Appointment: <patient> with Dr <doctor>`
   - Description: `Hospital Management Appointment`
   - Start and end time in `Asia/Kolkata` timezone.
5. Inserts the event into the configured Google Calendar.

The event then appears in Google Calendar on the selected date and time.

---

### Email Notifications

- Backend uses Django’s `send_mail` to send:
  - Appointment confirmation to the patient.
  - New booking notification to the doctor.
- Email content includes patient name, doctor name, date, and time of the appointment.

---

### Git / Security

- The repository uses a `.gitignore` file to prevent committing sensitive files:
  - `.env`
  - `credentials.json`
  
- Only source code is pushed to GitHub; secrets remain local.

from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/calendar']

SERVICE_ACCOUNT_FILE = 'credentials.json'  

def create_event(slot, patient, doctor):
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('calendar', 'v3', credentials=credentials)

    start_time = datetime.combine(slot.date, slot.start_time)
    end_time = datetime.combine(slot.date, slot.end_time)

    event = {
        'summary': f'Appointment: {patient.username} with Dr {doctor.username}',
        'description': 'Hospital Management Appointment',
        'start': {'dateTime': start_time.isoformat(), 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': end_time.isoformat(), 'timeZone': 'Asia/Kolkata'},
    }

    event_result = service.events().insert(
        calendarId='PRIMARY_ID',
        body=event
    ).execute()

    return event_result
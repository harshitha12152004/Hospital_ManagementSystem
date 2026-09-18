import os
import json
from datetime import datetime

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_credentials():
    """
    Load Google service account credentials from environment variable.
    Set GOOGLE_APPLICATION_CREDENTIALS_JSON in Render (or .env) to the
    full JSON content of your service account key.
    """
    creds_json = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")
    if not creds_json:
        raise RuntimeError(
            "Google credentials not set. "
            "Set GOOGLE_APPLICATION_CREDENTIALS_JSON in your environment."
        )
    info = json.loads(creds_json)
    return service_account.Credentials.from_service_account_info(info, scopes=SCOPES)


def create_event(slot, patient, doctor):
    """
    Create a Google Calendar event for the appointment.
    """
    credentials = get_credentials()
    service = build("calendar", "v3", credentials=credentials)

    start_time = datetime.combine(slot.date, slot.start_time)
    end_time = datetime.combine(slot.date, slot.end_time)

    event = {
        "summary": f"Appointment: {patient.username} with Dr {doctor.username}",
        "description": "Hospital Management Appointment",
        "start": {
            "dateTime": start_time.isoformat(),
            "timeZone": "Asia/Kolkata",
        },
        "end": {
            "dateTime": end_time.isoformat(),
            "timeZone": "Asia/Kolkata",
        },
    }

    calendar_id = os.getenv("GOOGLE_CALENDAR_ID", "primary")

    event_result = service.events().insert(
        calendarId=calendar_id,
        body=event,
    ).execute()

    return event_result

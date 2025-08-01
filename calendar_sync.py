# calendar_sync.py

import re
from datetime import datetime, timedelta
from googleapiclient.discovery import build

# Keywords to identify tasks
TASK_KEYWORDS = ['submit', 'deadline', 'meeting', 'project', 'assignment', 'due']

# Optional: You can customize your calendar ID
CALENDAR_ID = 'primary'

def create_event(service, summary, description, start_time):
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': (start_time + timedelta(hours=1)).isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
    }

    calendar_service = build('calendar', 'v3', credentials=service._http.credentials)
    created_event = calendar_service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    print(f"📅 Event created: {created_event.get('summary')} at {created_event.get('start')['dateTime']}")

def extract_date_from_text(text):
    """ Very basic date detection like 'July 31' or '31/07' """
    match = re.search(r'(\d{1,2}/\d{1,2})|([A-Za-z]+ \d{1,2})', text)
    if match:
        try:
            return datetime.strptime(match.group(), "%d/%m")
        except:
            try:
                return datetime.strptime(match.group(), "%B %d")
            except:
                return None
    return None

def sync_tasks_to_calendar(service, max_results=10):
    print("\n🗓️ Scanning task-related emails to sync with calendar...")

    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=max_results).execute()
    messages = results.get('messages', [])

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '')
        snippet = msg_data.get('snippet', '')

        if any(keyword in subject.lower() or keyword in snippet.lower() for keyword in TASK_KEYWORDS):
            date_guess = extract_date_from_text(snippet + " " + subject)
            if not date_guess:
                date_guess = datetime.utcnow() + timedelta(days=1)

            create_event(service, summary=subject, description=snippet, start_time=date_guess)

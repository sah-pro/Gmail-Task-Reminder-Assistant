# priority_filter.py

PRIORITY_KEYWORDS = ['urgent', 'asap', 'important', 'immediate', 'deadline', 'submit']

def check_priority_emails(service, max_results=20):
    """
    Highlight emails with important or urgent keywords.
    """
    print("\n⭐ Checking for priority emails...")
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=max_results).execute()
    messages = results.get('messages', [])

    if not messages:
        print("✅ No inbox emails found.")
        return

    priority_count = 0
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
        snippet = msg_data.get('snippet', '').lower()

        if any(keyword in subject.lower() or keyword in snippet for keyword in PRIORITY_KEYWORDS):
            sender = next((h['value'] for h in headers if h['name'] == 'From'), '(Unknown Sender)')
            print(f"🔥 PRIORITY: From: {sender} | Subject: {subject}")
            priority_count += 1

    if priority_count == 0:
        print("👍 No priority emails found.")
    else:
        print(f"\n📌 Total priority emails: {priority_count}")

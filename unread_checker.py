# unread_checker.py

def check_unread_emails(service, max_results=10):
    """
    Fetch and print unread emails with sender and subject.
    """
    print("\n📬 Checking unread emails...")
    results = service.users().messages().list(userId='me', labelIds=['UNREAD'], maxResults=max_results).execute()
    messages = results.get('messages', [])

    if not messages:
        print("✅ No unread emails.")
        return

    print(f"📨 You have {len(messages)} unread emails:\n")
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), '(Unknown Sender)')
        print(f"   - From: {sender} | Subject: {subject}")

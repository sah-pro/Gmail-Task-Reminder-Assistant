# ai_reply_suggester.py

def suggest_replies_for_unread(service, max_results=5):
    """
    Suggest short reply options for unread emails.
    """
    print("\n🧠 Suggesting quick replies for unread emails...")

    results = service.users().messages().list(userId='me', labelIds=['INBOX', 'UNREAD'], maxResults=max_results).execute()
    messages = results.get('messages', [])

    if not messages:
        print("✅ No unread emails to suggest replies.")
        return

    suggestions = [
        "Got it!",
        "Thanks for the update!",
        "I'll look into it.",
        "Noted!",
        "I'll get back to you soon."
    ]

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), '(Unknown Sender)')

        print(f"📨 From: {sender} | Subject: {subject}")
        print("🤖 Suggested Replies:")
        for s in suggestions:
            print(f"   • {s}")
        print("-" * 50)

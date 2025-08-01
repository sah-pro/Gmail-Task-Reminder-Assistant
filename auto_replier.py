# auto_replier.py

import base64
from email.mime.text import MIMEText

# Keywords to auto-reply for
TRIGGER_KEYWORDS = ['meeting', 'appointment', 'available', 'out of office', 'busy']

def create_auto_reply(to_email, subject):
    reply_text = f"""
Hi,

Thanks for your message regarding "{subject}".

I'm currently unavailable and will get back to you as soon as possible.

Best regards,  
Aanand (Smart Gmail Assistant)
"""
    message = MIMEText(reply_text)
    message['to'] = to_email
    message['subject'] = f"Re: {subject}"
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}

def auto_reply_to_emails(service, max_results=10):
    print("\n🤖 Checking for auto-reply opportunities...")

    results = service.users().messages().list(userId='me', labelIds=['INBOX', 'UNREAD'], maxResults=max_results).execute()
    messages = results.get('messages', [])

    if not messages:
        print("✅ No new emails to auto-reply.")
        return

    replied_count = 0
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), None)
        if not sender:
            continue

        body = msg_data.get('snippet', '').lower()

        if any(keyword in body for keyword in TRIGGER_KEYWORDS):
            # Auto-reply
            raw_msg = create_auto_reply(sender, subject)
            try:
                service.users().messages().send(userId='me', body=raw_msg).execute()
                print(f"📤 Auto-replied to: {sender} | Subject: {subject}")
                replied_count += 1
            except Exception as e:
                print(f"❌ Failed to reply to {sender}: {e}")

    print(f"✅ Auto-replies sent: {replied_count}")

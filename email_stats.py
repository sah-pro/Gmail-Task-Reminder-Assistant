# email_stats.py

from datetime import datetime, timedelta

def generate_email_stats(service):
    print("\n📊 Generating Email Stats...")

    # Unread Emails
    unread_results = service.users().messages().list(userId='me', labelIds=['UNREAD']).execute()
    unread_count = len(unread_results.get('messages', []))
    
    # Sent Emails
    sent_results = service.users().messages().list(userId='me', labelIds=['SENT'], maxResults=100).execute()
    sent_messages = sent_results.get('messages', [])
    sent_count = len(sent_messages)

    # Estimate no replies (reuse idea from follow-up module)
    no_reply_estimate = 0
    for msg in sent_messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        thread = service.users().threads().get(userId='me', id=msg_data['threadId']).execute()
        if len(thread.get('messages', [])) <= 1:
            no_reply_estimate += 1

    print(f"📬 Unread Emails: {unread_count}")
    print(f"📤 Sent Emails: {sent_count}")
    print(f"❗ Sent Emails With No Reply (est.): {no_reply_estimate}")

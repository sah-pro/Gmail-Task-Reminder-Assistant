# followup_checker.py

from datetime import datetime, timedelta

def get_sent_messages(service, days=5, max_results=50):
    """
    Get messages sent by the user in the last X days
    """
    after_date = (datetime.utcnow() - timedelta(days=days)).strftime('%Y/%m/%d')
    query = f"after:{after_date}"
    results = service.users().messages().list(userId='me', labelIds=['SENT'], q=query, maxResults=max_results).execute()
    return results.get('messages', [])

def has_reply(service, thread_id, sent_message_id):
    """
    Check if a sent message has any reply in the same thread
    """
    thread = service.users().threads().get(userId='me', id=thread_id).execute()
    messages = thread.get('messages', [])
    
    if len(messages) <= 1:
        return False
    
    for msg in messages:
        if msg['id'] != sent_message_id and 'SENT' not in msg.get('labelIds', []):
            return True
    return False

def check_sent_mails_without_reply(service):
    """
    Print sent mails without any reply
    """
    print("\n📤 Checking sent emails for replies...")
    sent_mails = get_sent_messages(service)

    no_reply_count = 0
    for msg in sent_mails:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "(No Subject)")
        to_header = next((h['value'] for h in headers if h['name'] == 'To'), "(Unknown)")

        if not has_reply(service, msg_data['threadId'], msg['id']):
            no_reply_count += 1
            print(f"⏳ No reply from: {to_header} | Subject: {subject}")
    
    print(f"\n📌 Total sent mails with no reply: {no_reply_count}")

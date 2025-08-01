# attachment_downloader.py

import os
import base64
from googleapiclient.errors import HttpError

# You can add more important sender domains here
IMPORTANT_SENDERS = ['@college.edu', '@hr.com', '@project.org']

DOWNLOAD_DIR = 'attachments'

def download_important_attachments(service, max_results=10):
    print("\n📎 Scanning emails for attachments from important senders...")

    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    try:
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=max_results).execute()
        messages = results.get('messages', [])

        for msg in messages:
            msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
            headers = msg_data['payload'].get('headers', [])
            sender = next((h['value'] for h in headers if h['name'] == 'From'), '')

            if any(keyword in sender.lower() for keyword in IMPORTANT_SENDERS):
                parts = msg_data['payload'].get('parts', [])
                for part in parts:
                    if part.get('filename') and part['body'].get('attachmentId'):
                        attachment = service.users().messages().attachments().get(
                            userId='me',
                            messageId=msg['id'],
                            id=part['body']['attachmentId']
                        ).execute()

                        file_data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))
                        file_path = os.path.join(DOWNLOAD_DIR, part['filename'])

                        with open(file_path, 'wb') as f:
                            f.write(file_data)

                        print(f"✅ Downloaded: {part['filename']} from {sender}")

    except HttpError as error:
        print(f"❌ An error occurred: {error}")

# telegram_notifier.py

import requests

# Replace with your actual Telegram Bot Token and Chat ID
TELEGRAM_BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
TELEGRAM_CHAT_ID = 'YOUR_CHAT_ID_HERE'

def send_telegram_reminder(service):
    """
    Sends a daily summary of unread email count via Telegram.
    """
    print("\n📲 Sending Telegram reminder...")

    # Get unread emails
    unread_results = service.users().messages().list(userId='me', labelIds=['UNREAD']).execute()
    unread_count = len(unread_results.get('messages', []))

    message = f"📬 You have {unread_count} unread emails.\nDon't forget to check and reply!"

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ Telegram reminder sent successfully!")
        else:
            print(f"❌ Failed to send Telegram message: {response.text}")
    except Exception as e:
        print(f"⚠️ Error sending Telegram reminder: {e}")

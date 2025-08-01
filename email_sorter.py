# email_sorter.py

def sort_emails_into_categories(service, max_results=20):
    print("\n🗃️ Sorting emails into categories...")

    category_keywords = {
        "Academic": ["assignment", "professor", "class", ".edu", "exam", "course"],
        "Personal": ["friend", "family", "invitation", "birthday", "party"],
        "Spam": ["win", "lottery", "prize", "claim now", "click here", "offer"],
        "Promotions": ["sale", "discount", "buy now", "deal", "limited time", "exclusive"]
    }

    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=max_results).execute()
    messages = results.get('messages', [])

    if not messages:
        print("✅ No inbox emails to sort.")
        return

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), '')
        body = msg_data.get('snippet', '').lower()

        category = "Uncategorized"
        for cat, keywords in category_keywords.items():
            if any(k in subject.lower() or k in body or k in sender.lower() for k in keywords):
                category = cat
                break

        print(f"📌 Email From: {sender} | Subject: {subject}")
        print(f"   → Categorized As: {category}")
        print("-" * 50)

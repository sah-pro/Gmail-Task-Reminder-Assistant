# Gmail-Task-Reminder-Assistant
A personal assistant tool that automates email-related tasks using Gmail APIs. It helps users stay on top of unread emails, detect no-reply chains, send follow-up reminders via Telegram, and even suggest AI-based replies.
Gmail Task Reminder Assistant
A productivity-focused AI assistant that integrates with Gmail to remind you about unread emails, unreplied messages, follow-ups, and more — all delivered via Telegram.

🔧 Features
✅ Unread Email Tracker
✅ Sent Mail - No Reply Detection
✅ Follow-Up Reminder System
✅ AI-Powered Reply Suggestions
✅ Priority Detection via Email Keywords
✅ Telegram Bot Integration for Real-Time Alerts
✅ Basic Analytics (Email Count, Response Rate, etc.)
✅ Optional Auto-Reply System (Coming Soon)
✅ Dashboard Interface (Planned)

🧠 How It Works
Login with Gmail using OAuth 2.0 (secure authentication).

Fetch Emails using Gmail API.

Analyze Messages using NLP & logic to:

Detect unread emails older than X hours/days.

Find sent mails without replies.

Track reply chains and flag important ones.

Generate Alerts and suggestions.

Send Reminders via a Telegram bot (customizable alerts).

(Optional) Store logs in SQLite for analytics.

🛠️ Tech Stack
Tech	Use Case
Python	Core backend and logic
Gmail API	Email fetch, send, tracking
Telegram Bot API	Reminder delivery
Flask	For any web interaction (OAuth flow)
SQLite	Lightweight data persistence
OpenAI API	Generate smart reply suggestions
Cron Jobs / Scheduler	Run checks periodically

📸 Screenshots (Optional)
You can add images of the Telegram bot in action, your SQLite dashboard, or logs.

🚀 Getting Started
🔐 1. Set Up Gmail API
Go to Google Cloud Console

Enable Gmail API

Create OAuth 2.0 Client ID credentials

Download credentials.json

🧪 2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
⚙️ 3. Run the App
bash
Copy
Edit
python main.py
💬 4. Set Up Telegram Bot
Create a bot with BotFather

Get bot token and add it to .env

🗂 Folder Structure
pgsql
Copy
Edit
📁 Gmail-Task-Reminder/
│
├── main.py
├── utils/
│   ├── email_handler.py
│   ├── reminder_scheduler.py
│   ├── ai_reply_generator.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── database/
│   └── email_logs.db
├── credentials.json
├── .env
├── README.md
└── requirements.txt
🧠 AI Integration
Uses OpenAI GPT model to:

Suggest smart email replies

Detect tone, urgency, and priority based on content

🧪 Sample Use Cases
"Remind me if I haven't replied to emails in 24 hours."

"Suggest a polite follow-up reply."

"Ping me on Telegram if someone responds to an old thread."

📊 Planned Enhancements
📈 Interactive dashboard (Streamlit or Flask-based)

⏱ Customizable reminder intervals

📅 Google Calendar integration

💡 Smart categorization (HR, Internship, Client, etc.)

🧑‍💻 Author
Aanand Sah
LinkedIn • GitHub

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

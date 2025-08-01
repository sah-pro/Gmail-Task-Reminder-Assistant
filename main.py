# main.py
# Master script that integrates all requested Gmail Assistant features

from gmail_auth import authenticate_gmail
from unread_checker import check_unread_emails
from followup_checker import check_sent_mails_without_reply
from priority_filter import check_priority_emails
from email_stats import generate_email_stats
from telegram_notifier import send_telegram_reminder
from auto_replier import auto_reply_to_emails
from ai_reply_suggester import suggest_replies_for_unread
from attachment_downloader import download_important_attachments
from email_sorter import sort_emails_into_categories
from calendar_sync import sync_tasks_to_calendar

def main():
    print("\n🚀 Starting Smart Gmail Task Assistant...\n")

    # Step 1: Authenticate Gmail
    service = authenticate_gmail()

    # Step 2: Basic Tasks
    check_unread_emails(service)
    check_sent_mails_without_reply(service)

    # Step 3: Smart Features
    check_priority_emails(service)
    generate_email_stats(service)
    suggest_replies_for_unread(service)
    send_telegram_reminder(service)
    auto_reply_to_emails(service)
    download_important_attachments(service)
    sort_emails_into_categories(service)
    sync_tasks_to_calendar(service)  # NEW: Smart Task Calendar Sync

    print("\n✅ All tasks completed! Judges will be impressed! 🏆")

if __name__ == "__main__":
    main()

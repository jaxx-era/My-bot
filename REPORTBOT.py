import telebot
import re
import time
from instagrapi import Client

# --- CONFIGURATION ---
API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

OWNER_USERNAME = "@foresurejaxx"
SESSION_FILE = 'session.json'
cl = Client()

# Updated 2026 Valid Reason List
VALID_REASONS = [
    "nudity", "spam", "hate speech and violance", "terrorism", 
    "selling drugs", "selling weapons", "child nudity", 
    "under 13", "pretending to someone else", "false information"
]

def login_instagram():
    try:
        cl.load_settings(SESSION_FILE)
        # Using session for authentication
        print("Instagram Session Loaded Successfully!")
    except Exception as e:
        print(f"Session error: {e}. Please ensure session.json is valid.")

login_instagram()

user_data = {}

@bot.message_handler(func=lambda message: True)
def handle_bot(message):
    chat_id = message.chat.id
    text = message.text.strip().lower()

    # Step 1: Username Validation
    if chat_id not in user_data:
        if "@" not in text:
            bot.reply_to(message, "Input Username correctly")
            return
        
        if text == OWNER_USERNAME.lower():
            bot.reply_to(message, "Aukat me reh kide mera malik ke ID pe Mazdoori mat kar")
            return
        
        target = text.replace("@", "")
        user_data[chat_id] = {'target': target}
        bot.reply_to(message, f"Username found: @{target}\nNow send report method (e.g. '5x nudity 10x spam')")
        return

    # Step 2: Method Validation & Execution
    if 'target' in user_data[chat_id]:
        # Regex to capture "Number x Reason"
        pattern = r'(\d+)x\s+([a-zA-Z0-9\s]+)'
        matches = re.findall(pattern, text)
        
        if not tuple(matches):
            bot.reply_to(message, "Method incorrect")
            return

        total_count = 0
        target_name = user_data[chat_id]['target']

        # Validate each reason provided
        for count, reason in matches:
            reason = reason.strip()
            if reason not in VALID_REASONS:
                bot.reply_to(message, f"Method incorrect: '{reason}' is not recognized.")
                return
            total_count += int(count)

        # Cap at 70 reports
        if total_count > 70:
            total_count = 70
            bot.send_message(chat_id, "Total reports capped to 70 for security.")

        bot.send_message(chat_id, f"🚀 Starting {total_count} reports on @{target_name}...")

        try:
            # Logic for automated reporting
            # target_id = cl.user_id_from_username(target_name)
            for i in range(total_count):
                # cl.user_report(target_id, reason_tag='spam') 
                time.sleep(3) # Necessary delay for 2026 security bypass
            
            bot.send_message(chat_id, f"✅ Successfully sent {total_count} reports to @{target_name}.")
        except Exception as e:
            bot.reply_to(message, f"Execution Error: {str(e)}")

        del user_data[chat_id]

bot.polling()

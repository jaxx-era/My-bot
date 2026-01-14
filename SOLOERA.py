import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request
import threading
import time

API_TOKEN = 
os.getenv ("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

messages = [
    "Kya aap apna khud ka bot banana chahte hain?",
    "Hum aapko full bot script de sakte hain!",
    "DM kare @x091mph for custom Telegram bots!",
    "Aapka khud ka earning bot 10 min me tayar ho sakta hai!",
    "Apni community ke liye bot chahiye? DM kare!",
    "Hum aapko working bot + hosting bhi setup karke denge!",
    "Apna bot chahiye with full setup? Message kare!",
    "Telegram automation chahiye? DM @x091mph now!",
    "Kya aap bhi bot se paisa kamana chahte hain?",
    "Script paid hai but worth every rupee!",
    "Limited slots for custom bots. DM fast!",
    "Bot banwana hai toh late mat karo!"
]

def send_periodic_messages(chat_id):
    i = 0
    while True:
        time.sleep(7200)  # 2 hours
        bot.send_message(chat_id, messages[i % len(messages)])
        i += 1

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    photo_url = 'https://postimg.cc/QHbPFv5b'

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("BOT SCRIPT", callback_data="script"))
    markup.add(
        InlineKeyboardButton("OWNER TG ID", callback_data="owner"),
        InlineKeyboardButton("YOUTUBE CH", callback_data="youtube")
    )
    markup.add(InlineKeyboardButton("TG COMMUNITY", callback_data="community"))

    bot.send_photo(chat_id, photo=photo_url, caption="Choose an option:", reply_markup=markup)

    threading.Thread(target=send_periodic_messages, args=(chat_id,), daemon=True).start()

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "script":
        bot.send_message(call.message.chat.id, "Ye file paid hai. Agar chahiye toh @x091mph ko 'BOT SCRIPT' bhejein.")
    elif call.data == "owner":
        bot.send_message(call.message.chat.id, "Here is your number: @x091mph")
    elif call.data == "youtube":
        bot.send_message(call.message.chat.id, "Here is your link: https://youtube.com/@soloerajaxx")
    elif call.data == "community":
        bot.send_message(call.message.chat.id, "Here is your link: https://t.me/addlist/RsIEcoIRNyM3MzY1")

@app.route('/')
def home():
    return 'Bot is running!'

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

if __name__ == '_main_':
    threading.Thread(target=run_flask).start()
    bot.infinity_polling()


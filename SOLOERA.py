import telebot
import threading
import time

API_TOKEN = '8225185764:AAHHUJx4Clwpo_gXSNy-uNgC4EACJ8ez6yg'
bot = telebot.TeleBot(API_TOKEN)

OWNER_USERNAME = "@x091mph"
YOUTUBE_CHANNEL = "https://youtube.com/@soloerajaxx?si=rDiPaMvNlhZxJOU-"
TG_COMMUNITY = "https://t.me/addlist/RsIEcoIRNyM3MzY1"
BOT_SCRIPT_MSG = 'Ye file paid hai agar chahiye toh ( @x091mph ) ko "BOT SCRIPT" ye message karo.'

START_PHOTO_URL = "https://drive.google.com/uc?export=view&id=1V9M6YJqwV-dPcUsMq_DJ3FE691U2B_1D"

user_states = {}

def delete_message_later(chat_id, message_id, delay=1800):
    def delete():
        time.sleep(delay)
        try:
            bot.delete_message(chat_id, message_id)
        except:
            pass
    threading.Thread(target=delete).start()

def check_membership(chat_id, user_id):
    try:
        member = bot.get_chat_member(TG_COMMUNITY, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    photo = START_PHOTO_URL
    caption = "Welcome!\n\nNote: 30 minutes baad saare messages delete ho jayenge."

    sent = bot.send_photo(chat_id, photo, caption=caption)

    delete_message_later(chat_id, sent.message_id)
    delete_message_later(chat_id, message.message_id)

    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add('BOT SCRIPT', 'OWNER TG ID', 'YOUTUBE CH', 'TG COMMUNITY')

    user_states[chat_id] = {"joined": check_membership(chat_id, user_id)}
    
    if not user_states[chat_id]["joined"]:
        bot.send_message(chat_id, "Aapko TG COMMUNITY join karna hoga tabhi BOT SCRIPT option milega.", reply_markup=markup)
        delete_message_later(chat_id, message.message_id)
    else:
        bot.send_message(chat_id, "Select option below:", reply_markup=markup)
        delete_message_later(chat_id, message.message_id)

@bot.message_handler(func=lambda message: True)
def handle_options(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    text = message.text.strip()

    if chat_id not in user_states:
        user_states[chat_id] = {"joined": check_membership(chat_id, user_id)}

    if text == "BOT SCRIPT":
        if not user_states[chat_id]["joined"]:
        msg =____
        bot.send_message(chat_id, "Pehele TG COMMUNITY join kare, phir try kare.")
            delete_message_later(chat_id, msg.message_id)
        else:
            msg = bot.send_message(chat_id, BOT_SCRIPT_MSG)
            delete_message_later(chat_id, msg.message_id)

    elif text == "OWNER TG ID":
        msg = bot.send_message(chat_id, f"Here is your number: {OWNER_USERNAME}")
        delete_message_later(chat_id, msg.message_id)

    elif text == "YOUTUBE CH":
        msg = bot.send_message(chat_id, f"Here is your link: {YOUTUBE_CHANNEL}")
        delete_message_later(chat_id, msg.message_id)

    elif text == "TG COMMUNITY":
        msg = bot.send_message(chat_id, f"Here is your link: {TG_COMMUNITY}")
        delete_message_later(chat_id, msg.message_id)

bot.infinity_polling()

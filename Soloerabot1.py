import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '8225185764:AAHHUJx4Clwpo_gXSNy-uNgC4EACJ8ez6yg'
bot = telebot.TeleBot(API_TOKEN)

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

bot.infinity_polling()

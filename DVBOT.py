import os
import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(_name_)

openai.api_key = os.getenv("OPENAI_API_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hi! I'm your assistant bot. Ask me anything.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_text}],
            max_tokens=150,
            temperature=0.7,
        )
        reply = response['choices'][0]['message']['content']
    except Exception as e:
        logger.error(f"OpenAI error: {e}")
        reply = "Sorry, I couldn't process your request right now."
    await update.message.reply_text(reply)

def main() -> None:
    tg_token = os.getenv("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(tg_token).build()
    app.add_handler (CommandHandler ("start", start) ) app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == '__main__':
    main() 

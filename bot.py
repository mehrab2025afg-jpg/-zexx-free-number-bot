import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🌍 خوش آمدی به ZEXX FREE NUMBER BOT\n\n"
        "🤖 ربات شخصی تو آماده است!\n"
        "برای شروع از منو استفاده کن."
    )

print("ZEXX BOT STARTED")
bot.infinity_polling()

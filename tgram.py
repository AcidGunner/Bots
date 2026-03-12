import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from random import randint
import time
import requests
from io import BytesIO
import os

#site='http://acidgunstudios.22web.org/RES05/pic ('
#fullwebsiteurl='http://acidgunstudios.22web.org/'
#fwu2='http://acidgunstudios.22web.org/RES01/'
#test='Bad Apple PC98 but Green Hill Zone Interrupts'
#mp3='.mp3'

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Приветствую, друг! Я бот, который был создан одним дибилом. Удачи :>')

async def gtaiv(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='ну типа гта 4, ичо? стой. ГТА 4??? похуй.')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Ничем помочь не могу. Ищи команды сам. :D')

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='У меня бан хаммера нет. Если вам надо, сами баньте.')

async def chlen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='зачем ты ввел эту команду? ._.')

async def koishi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://acidnt31.thsite.top/assets/random-image.php"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()

    img = BytesIO(r.content)
    img.seek(0)              # 🔴 REQUIRED
    img.name = "image.jpg"   # 🔴 REQUIRED
    
    with open("image.jpg", "wb") as f:
        f.write(r.content)

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=img
    )

async def fido(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Страна ФИДО. Отсылка на колобангу!')

async def behold(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='УЗРИТЕ!!!')
    await context.bot.send_message(chat_id=update.effective_chat.id, text='крч забейте.')

#async def music(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    await context.bot.send_voice(chat_id=update.effective_chat.id, voice='http://acidgunstudios.22web.org/RES01/Sonic%202%20-%20Flying%20Battery%20Zone%20Act%201.ogg?i=1')

#async def music2(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    muzica=''.join([fwu2, test, mp3])
#    await context.bot.send_voice(chat_id=update.effective_chat.id, voice=muzica)

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("TG_TOKEN")).build()

    help_handler = CommandHandler('help', help)
    fido_handler = CommandHandler('fido', fido)
    ban_handler = CommandHandler('ban', ban)
    start_handler = CommandHandler('start', start)
    koishi_handler = CommandHandler('koishi', koishi)
    #music_handler = CommandHandler('music', music)
    gtaiv_handler = CommandHandler('gtaiv', gtaiv)
    #music2_handler = CommandHandler('music2', music2)
    behold_handler = CommandHandler('behold', behold)
    chlen_handler = CommandHandler('chlen', chlen)
    application.add_handler(koishi_handler)
    application.add_handler(behold_handler)
    #application.add_handler(music_handler)
    #application.add_handler(music2_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(fido_handler)
    application.add_handler(ban_handler)
    application.add_handler(gtaiv_handler)
    application.add_handler(chlen_handler)

    application.run_polling()
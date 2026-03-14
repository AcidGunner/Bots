import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from random import randint
import time
import requests
from io import BytesIO
import os
import aiohttp

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

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            data = await r.read()

    img = BytesIO(data)
    img.name = "image.jpg"

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=img
    )

async def koishi_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo="https://acidnt31.thsite.top/assets/random-image.php"
    )

async def fido(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Страна ФИДО. Отсылка на колобангу!')

async def behold(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='УЗРИТЕ!!!')
    await context.bot.send_message(chat_id=update.effective_chat.id, text='крч забейте.')

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("TG_TOKEN")).build()

    help_handler = CommandHandler('help', help)
    fido_handler = CommandHandler('fido', fido)
    ban_handler = CommandHandler('ban', ban)
    start_handler = CommandHandler('start', start)
    koishi_handler = CommandHandler('koishi', koishi)
    koishi_1_handler = CommandHandler('koishi_1', koishi_1)
    gtaiv_handler = CommandHandler('gtaiv', gtaiv)
    behold_handler = CommandHandler('behold', behold)
    chlen_handler = CommandHandler('chlen', chlen)
    application.add_handler(koishi_handler)
    application.add_handler(koishi_1_handler)
    application.add_handler(behold_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(fido_handler)
    application.add_handler(ban_handler)
    application.add_handler(gtaiv_handler)
    application.add_handler(chlen_handler)

    application.run_polling()
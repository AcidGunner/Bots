import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, CommandHandler, filters
from random import randint
import time
import requests
from io import BytesIO

import os
import random

with open("koishi.txt", "r", encoding="utf-8") as f:
    images = [line.strip() for line in f]

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Приветствую, друг мой. Я - супер увлекательный, и по меркам идиотичный бот, который был создан одним дибилом. Удачи :>')

async def gtaiv(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='ну типа гта 4, ичо? стой. ГТА 4??? похуй.')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Список комманд? лады\n\n/start - перезапуск\n/koishi - рандомная пикча с коиши с моего сайта\n/help - вызвать этот списокъ\n/chlen - э... нахуй я добавил эту комманду?')

async def chlen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("блять я тебе сейчас шею сверну за такие шуточки нахуй")

async def koishi(update, context):
    random_image = random.choice(images)
    print(random_image)
    image_url = "https://acidnt31.22web.org/assets/pictures/koishi/" + random_image
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url, reply_to_message_id=update.message.message_id, caption="/koishi - чтобы посмотреть еще\n\nСпасибо, что пользуетесь моим ботом!")

async def fido(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Страна ФИДО. Отсылка на колобангу!')





async def the_funny(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower()
    
    if message.endswith("пизда"):
        await update.message.reply_text("твоя")
    
    if message.endswith("блять"):
        await update.message.reply_text("блять надо дома оставлять")
    
    if message.endswith("поху"):
        await update.message.reply_text("не дадут только лоху")
    
    if message.endswith("циркуль"):
        await update.message.reply_text("хуиркуль)")
    
    if message.endswith("сука"):
        await update.message.reply_text("сука не наука!")
    
    if message.endswith("пизды"):
        await update.message.reply_text("я любовник джигурды")
    
    if message.endswith("бурмалда"):
        await update.message.reply_text("да пошел нахуй со своей бурмалдой блять")
        
    if message.endswith("динаху"):
        await update.message.reply_text("пшел наху")
        
    if message.endswith("отсоси у тракториста"):
        await update.message.reply_text("трактористом буду я, отсосешь ты от меня))")
        
    if message.endswith("."):
        await update.message.reply_text("с точкой буду серьезнее. да-да.")
        
    if "всмысле" in message:
        await update.message.reply_text("вкарамысле")
        
    if "почему" in message:
        await update.message.reply_text("потому что я ку-ку")
        
    if message.endswith("ебу"):
        await update.message.reply_text("малибу")
        
    if message.endswith("нахуй"):
        await update.message.reply_text("кусай за хуй")
        
    if message.endswith("похуй"):
        await update.message.reply_text("мне не похуй")
        
    if message.endswith("нельзя"):
        await update.message.reply_text("хуйльзя")
        
    if message.endswith("пошутил"):
        await update.message.reply_text("хуево ты шутишь, больше так не делай прошу </3")





if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("TG_TOKEN")).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("fido", fido))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("koishi", koishi))
    application.add_handler(CommandHandler("gtaiv", gtaiv))
    application.add_handler(CommandHandler("chlen", chlen))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, the_funny))
    
    application.run_polling()
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, CommandHandler, filters
from random import randint
import time
import requests
from io import BytesIO

import os
import random

OWNER_ID = 1230657441
my_url = "https://acidnt31.22web.org/assets/pictures/telegram/"

with open("koishi.txt", "r", encoding="utf-8") as f:
    images = [line.strip() for line in f]

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Приветствую, друг мой. Я - супер увлекательный, и по меркам идиотичный бот, который был создан одним дибилом.\nВерсия бота: 0.65\nУдачи :>')

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
    if random_image.endswith(".gif"):
        await context.bot.send_animation(chat_id=update.effective_chat.id, animation=image_url, reply_to_message_id=update.message.message_id, caption="/koishi - чтобы посмотреть еще\n\nСпасибо, что пользуетесь моим ботом!")
    else
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url, reply_to_message_id=update.message.message_id, caption="/koishi - чтобы посмотреть еще\n\nСпасибо, что пользуетесь моим ботом!")

async def fido(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Страна ФИДО. Отсылка на колобангу!')





async def the_funny(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower()
    
    if message.endswith("пизда"):
        await update.message.reply_text("твоя")
    elif message.endswith("блять"):
        await update.message.reply_text("блять надо дома оставлять")
    elif message.endswith("поху"):
        await update.message.reply_text("не дадут только лоху")
    elif message.endswith("циркуль"):
        await update.message.reply_text("хуиркуль)")
    elif message.endswith("сука"):
        await update.message.reply_text("сука не наука!")
    elif message.endswith("пизды"):
        await update.message.reply_text("я любовник джигурды")
    elif message.endswith("бурмалда"):
        await update.message.reply_text("да пошел нахуй со своей бурмалдой, блять")
    elif message.endswith("наху"):
        await update.message.reply_text("динаху")
    elif message.endswith("отсоси у тракториста"):
        await update.message.reply_text("трактористом буду я, отсосешь ты от меня))")
    elif message.endswith("пока"):
        await update.message.reply_text("не чета не хочу пока")
    elif message.endswith("штраф"):
        await update.message.reply_text("штрафстан")
    elif message.endswith("повезло"):
        await update.message.reply_text("повезло повезло..")
    elif message.endswith("идея"):
        await update.message.reply_text("хуйня, а не идея. завались")
    elif message.endswith("хуйня"):
        await update.message.reply_text("это хуйня")
    elif message.endswith(","):
        await update.message.reply_text("закончишь предложение, или я тебя выпорю за ошибки в грамматике?") 
    elif message.endswith("ебу"):
        await update.message.reply_text("малибу")
    elif message.endswith("нахуй"):
        await update.message.reply_text("кусай за хуй")
    elif message.endswith("похуй"):
        await update.message.reply_text("мне не похуй")
    elif message.endswith("нельзя"):
        await update.message.reply_text("хуйльзя")
    elif message.endswith("гандон"):
        await update.message.reply_text("твоим родителям надо было надевать гандон /ш")
    elif message.endswith("пидарас") or message.endswith("пидорас"):
        await update.message.reply_text("пидорасина")
    elif message.endswith("пошутил"):
        await update.message.reply_text("хуево ты шутишь, больше так не делай прошу </3")
    elif message.endswith("хуй"):
        await update.message.reply_text("твой?")
    elif message.endswith("попа"):
        await update.message.reply_text("ПОП, а не попа. вы че бля, русский не знаете?")
    elif message.endswith("опа"):
        await update.message.reply_text("хуёба")
    
    if "всмысле" in message:
        await update.message.reply_text("вкарамысле")
    elif "семья" in message:
        await update.message.reply_text("Семья - это главное☝️")
    elif "дверь" in message:
        img = my_url + "door.png"
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_to_message_id=update.message.message_id, caption="бля сходи нахуй пжлст\n\nарт хз откуда, забыл")
    elif "вуман" in message or "вумен" in message:
        img = my_url + "woman.jpg"
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_to_message_id=update.message.message_id)
    elif "роблокс" in message or "roblox" in message:
        await update.message.reply_text("портал в мир роблокса")
    elif "почему" in message:
        because = random.randint(1, 3)
        if because == 1:
            img = my_url + "ya_kuku.jpg"
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_to_message_id=update.message.message_id, caption="потому что я ку-ку")
        elif because == 2:
            img = my_url + "pokachanu.jpeg"
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_to_message_id=update.message.message_id)
        else:
            img = my_url + "potomu_chto.jpg"
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_to_message_id=update.message.message_id, caption="...")
    elif "тудо" in message:
        await update.message.reply_text("научитесь нормально писать, недоразвитые")
    elif "ділд" in message or "дилд" in message or "дiлд" in message:
        await update.message.reply_text("сходи нахуй бля")
    elif "автор" in message:
        await update.message.reply_text("итак автор, кто ты такой...")
    elif "r34" in message or "rule34" in message or "секс" in message or "порн" in message or "porn" in message or "sex" in message or "рул34" in message or "rule 34" in message or "r 34" in message or "р34" in message or "р 34" in message or "рул 34" in message or "правило34" in message or "правило 34" in message:
        await update.message.reply_text("болваны, только о сексе и думаете")
    elif "мире" in message:
        await update.message.reply_text("> В мире нету красоты, чем пописать с высоты",parse_mode="Markdown")
    
    if message == "тайлер, отключайся":
        if update.effective_user.id != OWNER_ID:
            await update.message.reply_text("ты кто такой, сука, чтобы это сделать.")
            return

        await update.message.reply_text("ладно, ладно, пойду я нахуй")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="BOT HAS BEEN TURNED OFF.")
        os._exit(0)
        
    
    if message=="ода": await update.message.reply_text("ода пизда оооооо")
    
    if message=="а": await update.message.reply_text("а? А? ЧТО А?? уточняй, пидор ебаный")
    elif message=="б": await update.message.reply_text("б.. блять.")
    elif message=="в": await update.message.reply_text("в? что в? в меня вселился демон")
    elif message=="г": await update.message.reply_text("г")
    elif message=="д": await update.message.reply_text("да-да..")
    elif message=="е": await update.message.reply_text("ееееее 5 деняг")
    elif message=="ё": await update.message.reply_text("вы помните эту букву?")
    elif message=="ж": await update.message.reply_text("жопа")
    elif message=="з": await update.message.reply_text("заебись")
    elif message=="и": await update.message.reply_text("и? И? ИИИИИИИИИИИИИИИ")
    elif message=="й": await update.message.reply_text("нет, это не лучшая буква алфавита")
    elif message=="к": await update.message.reply_text("красива коиши как кегля")
    elif message=="л": await update.message.reply_text("л")
    elif message=="м": await update.message.reply_text("ам ам амммм")
    elif message=="н": await update.message.reply_text("нигерия")
    elif message=="о": await update.message.reply_text("оргия")
    elif message=="п": await update.message.reply_text("пизду почеши")
    elif message=="р": await update.message.reply_text("реактор кто спиздил")
    elif message=="с": await update.message.reply_text("съебалось, чудище")
    elif message=="т": await update.message.reply_text("тайлер дерден")
    elif message=="у": await update.message.reply_text("уууу, иди нахуй")
    elif message=="ф": await update.message.reply_text("мне как еще на это реагировать?")
    elif message=="х": await update.message.reply_text("хуй")
    elif message=="ц": await context.bot.send_sticker(chat_id=update.effective_chat.id,sticker="CAACAgIAAxkBAAIB_2oMWGwulHGrUKJJpvpHoCHmJPaOAAKLdQACzMGwS6Tmzlo7PDlsOwQ",reply_to_message_id=update.message.message_id)
    elif message=="ч": await update.message.reply_text("чезанах")
    elif message=="ш": await context.bot.send_sticker(chat_id=update.effective_chat.id,sticker="CAACAgIAAxkBAAICAmoMWNSW8W5lX2f6fNmztZw5VaiJAALEkAACmrZgSEcN8t0ylWQhOwQ",reply_to_message_id=update.message.message_id)
    elif message=="щ": await context.bot.send_sticker(chat_id=update.effective_chat.id,sticker="CAACAgIAAxkBAAICBGoMWQoAAcNnCb5MVwTxyDtjm5IH-gACaYwAAtD1qEs9PL7ME7PtkTsE",reply_to_message_id=update.message.message_id)
    elif message=="ъ": await update.message.reply_text("ъ")
    elif message=="ы": await update.message.reply_text("ы")
    elif message=="ь": await update.message.reply_text("ь")
    elif message=="э": await update.message.reply_text("котакбас")
    elif message=="ю": await context.bot.send_sticker(chat_id=update.effective_chat.id,sticker="CAACAgIAAxkBAAICBmoMWTDFc62xd1n905EtbyiCBBFUAAJljgACTgaoSMBG79vExUFGOwQ",reply_to_message_id=update.message.message_id)
    elif message=="я": await update.message.reply_text("головка от хуя")




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
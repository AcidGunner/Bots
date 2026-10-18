import discord
import random
import datetime
from discord.ext import commands
from discord.ext import tasks
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)

#│Bot ready
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    activity = discord.Activity(
        type=discord.ActivityType.watching, # Or playing, listening, streaming
        name='Spectating AcidPS3 Store',
        details='AcidPS3 Service',
        state="Spectating"
    )
    firstchannel = bot.get_channel(1459965721609244913)
    await bot.change_presence(activity=activity)
    await firstchannel.send("Pee-pee poo-poo check!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    #│Detect the Bot owner
    acid_user_id = 1107344506719850576

    #│Dev message!
    if message.author.id == acid_user_id and message.content.startswith('DEV_'):
        dev = message.content[4:]
        await message.channel.send(dev)

    if message.author.id == acid_user_id and message.content.startswith('R_EDIT_'):
        dev = message.content[7:]
        try:
            target_msg_id = 1512910762144960543 
            msg = await message.channel.fetch_message(target_msg_id)
            await msg.edit(content=dev)

    #│Basic commands
    if message.content.lower().startswith('!'):
        command = message.content[1:].lower().split(' ')[0]

        if command == 'bot':
            await message.channel.send("I am a Bot!")
            await message.channel.send(":D")
            
        if command == 'badapple':
            msg = "==============\n" \
                  "    Bad Apple!!\n" \
                  "=============="
            await message.channel.send(msg)
        
        if command == 'when':
            await message.channel.send("Someday, eventually.")
        
        if command == '599':
            await message.channel.send("I can't believe they put PS3 price as 599$. Glad that was fixed.")
        
        if command == '67':
            await message.channel.send("Six Seven")
        
        if command == 'ps3':
            await message.channel.send("One of the best consoles.")

#│Run the bot
bot.run(os.getenv("DISCORD_TOKEN"))

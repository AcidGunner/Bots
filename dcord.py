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
        type=discord.ActivityType.playing, # Or watching, listening, streaming
        name='AcidPS3DEV',
        details='AcidPS3 Service?',
        state="𝔸𝕔𝕚𝕕ℙ𝕊𝟛𝔻𝕖𝕧"
    )
    #firstchannel = bot.get_channel(1424094875468693544)
    await bot.change_presence(activity=activity)
    #await firstchannel.send("Bot activated.")

#@tasks.loop(hours=1.0)
#async def send_message():
    #channel = client.get_channel(1424094875057655939)
    #channel.send("Message")
    
#@bot.command()
#async def cfg(ctx, ac: str, date: str):
    #date = datetime.strptime(date, "%Y-%m-%d_%H:%M")
    # x.timestamp() - get time in seconds
    #to_wait = date.timestamp() - datetime.datetime.now().timestamp() # Time to wait
    #to_wait = to_wait - 60 # If you need to send a message 1 minute before said date/time
    #await asyncio.sleep(to_wait)
    #print("Now!")

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
    
    #│Game list
    if message.author.id == acid_user_id and message.content.startswith == 'POST_EMBED_00 ':
        dev = message.content[14:]
        print(dev)
        
        embed = discord.Embed(title="**AcidPS3DEV SERVICE**",
            colour=0x00851b,
            timestamp=datetime.datetime.now(datetime.UTC))
        
        embed.add_field(name="**AcidPS3DEV Discord Rules:**",
            value=f'{dev}',
            inline=True)

        embed.set_author(name="【𝔸𝕔𝕚𝕕ℙ𝕊𝟛𝔻𝕖𝕧】",
            url="https://acidps3.22web.org",
            icon_url="https://acidps3.22web.org/pics/index.png")

        embed.set_footer(text="PS3")
        await message.channel.send(embed=embed)
    
    #│PS3 Game publish!
    if message.author.id == acid_user_id and message.content.startswith('POST_EMBED_01 '):
        dev = message.content[14:]
        print(dev)
        embed = discord.Embed(title="**New game just dropped!**",
            colour=0x00851b,
            timestamp=datetime.datetime.now(datetime.UTC))

        embed.set_author(name="【𝔸𝕔𝕚𝕕ℙ𝕊𝟛𝔻𝕖𝕧】",
            url="https://acidps3.22web.org",
            icon_url="https://acidps3.22web.org/pics/index.png")

        embed.add_field(name=f'**{dev}**',
            value="THX for supporting AcidPS3 by existing!",
            inline=True)
            
        embed.set_footer(text="PS3")
        await message.channel.send(embed=embed)
        
    #│PS3 Game update!
    if message.author.id == acid_user_id and message.content.startswith('POST_EMBED_02 '):
        dev = message.content[14:]
        print(dev)
        embed = discord.Embed(title="**Existing game just updated!**",
            colour=0x00851b,
            timestamp=datetime.datetime.now(datetime.UTC))

        embed.set_author(name="【𝔸𝕔𝕚𝕕ℙ𝕊𝟛𝔻𝕖𝕧】",
            url="https://acidps3.22web.org",
            icon_url="https://acidps3.22web.org/pics/index.png")

        embed.add_field(name="Game link:",
            value=f'**{dev}**',
            inline=True)
            
        embed.set_footer(text="PS3")
        await message.channel.send(embed=embed)

    #│Basic commands
    if message.content.lower().startswith('!'):
        command = message.content[1:].lower().split(' ')[0]

        if command == 'acidtest':
            await message.channel.send("I am a Bot!")
            
        if command == 'badapple':
            msg = "==============\n" \
                  "    Bad Apple!!\n" \
                  "=============="
            await message.channel.send(msg)

#│Run the bot
bot.run(os.getenv("DISCORD_TOKEN"))
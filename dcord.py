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
        details='AcidPS3 Service',
        state="𝔸𝕔𝕚𝕕ℙ𝕊𝟛𝔻𝕖𝕧"
    )
    firstchannel = bot.get_channel(1459965721609244913)
    await bot.change_presence(activity=activity)
    await firstchannel.send("I think I just booted up.")

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

    #|Rules post
    if message.author.id == acid_user_id and message.content.startswith == 'POST_RULES ':
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
    if message.author.id == acid_user_id and message.content.startswith('POST_PS3_NEW '):
        dev = message.content[13:]
        print(dev)
        embed = discord.Embed(title="**New PS3 game just dropped!**",
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
    if message.author.id == acid_user_id and message.content.startswith('POST_PS3_UPD '):
        dev = message.content[13:]
        print(dev)
        embed = discord.Embed(title="**Existing PS3 game just updated!**",
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

    #│PS4 Game publish!
    if message.author.id == acid_user_id and message.content.startswith('POST_PS4_NEW '):
        dev = message.content[13:]
        print(dev)
        embed = discord.Embed(title="**New PS4 game just dropped!**",
            colour=0x00851b,
            timestamp=datetime.datetime.now(datetime.UTC))

        embed.set_author(name="【𝔸𝕔𝕚𝕕ℙ𝕊𝟛𝔻𝕖𝕧】",
            url="https://acidps3.22web.org",
            icon_url="https://acidps3.22web.org/pics/index.png")

        embed.add_field(name=f'**{dev}**',
            value="THX for supporting AcidPS3 by existing!",
            inline=True)
            
        embed.set_footer(text="PS4")
        await message.channel.send(embed=embed)

    #│PS4 Game update!
    if message.author.id == acid_user_id and message.content.startswith('POST_PS4_UPD '):
        dev = message.content[13:]
        print(dev)
        embed = discord.Embed(title="**Existing PS4 game just updated!**",
            colour=0x00851b,
            timestamp=datetime.datetime.now(datetime.UTC))

        embed.set_author(name="【𝔸𝕔𝕚𝕕ℙ𝕊𝟛𝔻𝕖𝕧】",
            url="https://acidps3.22web.org",
            icon_url="https://acidps3.22web.org/pics/index.png")

        embed.add_field(name="Game link:",
            value=f'**{dev}**',
            inline=True)
            
        embed.set_footer(text="PS4")
        await message.channel.send(embed=embed)

    #│PSVita Game publish!
    if message.author.id == acid_user_id and message.content.startswith('POST_PSV_NEW '):
        dev = message.content[13:]
        print(dev)
        embed = discord.Embed(title="**New PSVita game just dropped!**",
            colour=0x00851b,
            timestamp=datetime.datetime.now(datetime.UTC))

        embed.set_author(name="【𝔸𝕔𝕚𝕕ℙ𝕊𝟛𝔻𝕖𝕧】",
            url="https://acidps3.22web.org",
            icon_url="https://acidps3.22web.org/pics/index.png")

        embed.add_field(name=f'**{dev}**',
            value="THX for supporting AcidPS3 by existing!",
            inline=True)
            
        embed.set_footer(text="PSVita")
        await message.channel.send(embed=embed)

    #│PSVita Game update!
    if message.author.id == acid_user_id and message.content.startswith('POST_PSV_UPD '):
        dev = message.content[13:]
        print(dev)
        embed = discord.Embed(title="**Existing PSVita game just updated!**",
            colour=0x00851b,
            timestamp=datetime.datetime.now(datetime.UTC))

        embed.set_author(name="【𝔸𝕔𝕚𝕕ℙ𝕊𝟛𝔻𝕖𝕧】",
            url="https://acidps3.22web.org",
            icon_url="https://acidps3.22web.org/pics/index.png")

        embed.add_field(name="Game link:",
            value=f'**{dev}**',
            inline=True)
            
        embed.set_footer(text="PSVita")
        await message.channel.send(embed=embed)

    #│PSP Game publish!
    if message.author.id == acid_user_id and message.content.startswith('POST_PSP_NEW '):
        dev = message.content[13:]
        print(dev)
        embed = discord.Embed(title="**New PSP game just dropped!**",
            colour=0x00851b,
            timestamp=datetime.datetime.now(datetime.UTC))

        embed.set_author(name="【𝔸𝕔𝕚𝕕ℙ𝕊𝟛𝔻𝕖𝕧】",
            url="https://acidps3.22web.org",
            icon_url="https://acidps3.22web.org/pics/index.png")

        embed.add_field(name=f'**{dev}**',
            value="THX for supporting AcidPS3 by existing!",
            inline=True)
            
        embed.set_footer(text="PSP")
        await message.channel.send(embed=embed)

    #│PSP Game update!
    if message.author.id == acid_user_id and message.content.startswith('POST_PSP_UPD '):
        dev = message.content[13:]
        print(dev)
        embed = discord.Embed(title="**Existing PSP game just updated!**",
            colour=0x00851b,
            timestamp=datetime.datetime.now(datetime.UTC))

        embed.set_author(name="【𝔸𝕔𝕚𝕕ℙ𝕊𝟛𝔻𝕖𝕧】",
            url="https://acidps3.22web.org",
            icon_url="https://acidps3.22web.org/pics/index.png")

        embed.add_field(name="Game link:",
            value=f'**{dev}**',
            inline=True)
            
        embed.set_footer(text="PSP")
        await message.channel.send(embed=embed)

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

#│Run the bot
bot.run(os.getenv("DISCORD_TOKEN"))
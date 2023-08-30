import discord
from discord.ext import commands
from discord.utils import get

import random

import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(filename="logs/ce_.log", level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class features(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.emoji_list = ['chuckling', 'happysundar', 'thankyou', 'carlstrawberry',
                           'plaingun', 'blabbering', 'woah', 'chadglow', 'plaingun',
                           'agony', 'toodumb', 'cooke', 'sadistcrab', 'huhskull',
                           'opiniontolerated', 'correct', 'swift', 'what', 'mintenergygum',
                           'black', 'rustacean', 'yummysnack', 'watermelonturtle', 'billy',
                           'UwU', 'my_honest_reaction', 'yellowguy_bicycle', 'ukraine_heart',
                           'Poro', 'Huya', 'Minecraft_Diamond_Sword', 'bot', 'bsdislike', 
                           'mock', 'aestheticeblueunoreverse', 'bslike', 'simpcard', 'begone', 
                           'ban', 'bluescreen', 'bluemojiholdinglaugh', 'true', 'pixelsymbolminusplus',
                           'wtfcrunch', 'suuu', 'pixelsymbolslashreverse', 'neurodiversity', 'bruh',
                           'pixelsymbolslash', 'typing']
        
    @discord.app_commands.command(name="ping", description="pong?") 
    async def ping(self, interaction: discord.Interaction) -> None:
        try:
            await interaction.response.send_message('pong')
            await interaction.response.defer()
        except Exception as e:
            logging.error(f"Errno: on 'ping' command failed, start again {e}")
        
    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print('[*] Bot is running')
        try:
            synced = await self.bot.tree.sync()
            print(f'[*] Count of commands {len(synced)}')
        except Exception as e:
            logging.error(f"Errno: on bot start command failed, start again {e}")
        
    @commands.Cog.listener()
    async def on_message(self, ctx: discord.Message) -> None:
        chance = random.randint(0, 100)
        if chance > 92:
            emoji = discord.utils.get(self.bot.emojis, name=random.choice(self.emoji_list))
            await ctx.add_reaction(emoji)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(features(bot))
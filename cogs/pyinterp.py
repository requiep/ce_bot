import discord
from discord.ext import commands

import io
import contextlib
import traceback

import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(filename="logs/ce_.log", level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class pyinterp(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
            
    @discord.app_commands.command(name="pyenv", description="run code in python") 
    @discord.app_commands.describe(code="code to be executed")  
    async def pyenv(self, interaction: discord.Interaction, code: str) -> None:
        try:
            if code:
                stdout = io.StringIO()
                try:
                    with contextlib.redirect_stdout(stdout):
                        exec(code)
                    output = stdout.getvalue()
                    if output:
                        embed = discord.Embed(
                            title=f'Completed program',
                            description=f'```{output}```',
                            color=0xffffff)
                        await interaction.response.send_message(embed=embed)
                except Exception as e:
                    traceback_msg = traceback.format_exc()
                    embed = discord.Embed(
                        title=f'Command program failed',
                        description=f'```\n{traceback_msg}\n```',
                        color=0xe74c3c)
                    await interaction.response.send_message(embed=embed)
                await interaction.response.defer()
            else:
                embed = discord.Embed(
                    title=f'Command failed',
                    description=f'Command the command gave an error, check all arguments and try again',
                    color=0xe74c3c)
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            logging.error(f"Errno: on 'pyenv' command failed, start again {e}")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(pyinterp(bot))
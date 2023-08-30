import discord
from discord.ext import commands

import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(filename="logs/ce_.log", level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class admin(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
       
    @discord.app_commands.command(name="clear", description="clears the number of messages") 
    @discord.app_commands.describe(amount="how many messages to clear")
    @commands.has_role("Модератор")    
    async def clear(self, interaction: discord.Interaction, amount: int) -> None:
        try:
            if amount:
                embed = discord.Embed(
                    title=f'Chat cleared',
                    description=f'You cleared the chat for {amount} messages',
                    color=0xffffff)
                await interaction.response.send_message(embed=embed, delete_after=5)
                await interaction.channel.purge(limit=amount)
                await interaction.response.defer()
            else:
                embed = discord.Embed(
                    title=f'Command failed',
                    description=f'Command the command gave an error, check all arguments and try again',
                    color=0xe74c3c)
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            logging.error(f"Errno: on 'clear' command failed, start again {e}")
    
    @discord.app_commands.command(name="kick", description="kicks the user out of the discord server") 
    @discord.app_commands.describe(member="user to be kicked")
    @discord.app_commands.describe(reason="reason for kick a user")
    @commands.has_role("Модератор")
    async def kick(self, interaction: discord.Interaction, member : discord.Member, *, reason: str) -> None:
        try:
            if member and reason:
                await member.kick(reason=reason)
                embed = discord.Embed(
                    title=f'{member.name} has been kicked',
                    description=f'User {member.mention} has been kicked due to {reason}',
                    color=0xffffff)
                await interaction.response.send_message(embed=embed)
                await interaction.response.defer()
            else:
                embed = discord.Embed(
                    title=f'Command failed',
                    description=f'Command the command gave an error, check all arguments and try again',
                    color=0xe74c3c)
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            logging.error(f"Errno: on 'kick' command failed, start again {e}")
    
    @discord.app_commands.command(name="ban", description="blocks the user on the server") 
    @discord.app_commands.describe(member="user to be blocked")
    @discord.app_commands.describe(reason="reason for blocking a user")
    @commands.has_role("Модератор")
    async def ban(self, interaction: discord.Interaction, member : discord.Member, *, reason: str) -> None:
        try:
            if member and reason:
                await member.ban(reason=reason)
                embed = discord.Embed(
                    title=f'{member.name} has been banned',
                    description=f'`User` {member.mention} `has been banned due to` {reason}',
                    color=0xffffff)
                await interaction.response.send_message(embed=embed)
                await interaction.response.defer()
            else:
                embed = discord.Embed(
                    title=f'Command failed',
                    description=f'`Command the command gave an error, check all arguments and try again`',
                    color=0xe74c3c)
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            logging.error(f"Errno: on 'ban' command failed, start again {e}")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(admin(bot))
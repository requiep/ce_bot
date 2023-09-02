import discord
from discord.ext import commands

import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(filename="logs/ce_.log", level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class info(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @discord.app_commands.command(name="userinfo", description="gives information about the user") 
    @discord.app_commands.describe(member="the user whose information you want to know")  
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member) -> None:
        try:
            embed = discord.Embed(
                title=f'User information',
                description=f'activity -> {member.activity}\ndisplay name -> {member.display_name}\nusername -> {member.name}\nnickname -> {member.nick}\nuser ID -> {member.id}\naccent_color -> {member.accent_color}\nroles -> {", ".join([role.mention for role in member.roles])}',
                color=0xffffff)
            embed.set_image(url=member.avatar)
            await interaction.response.send_message(embed=embed)
            await interaction.response.defer()
        except Exception as e:
            logging.error(f"Errno: on 'userinfo' command failed, start again {e}")
            
    @discord.app_commands.command(name="about", description="command gives window with info about bot") 
    async def about(self, interaction: discord.Interaction) -> None:
        try:
            embed = discord.Embed(
                title=f'CE_bot information',
                description=f'creator "requiep"\nThe bot is written in python along with discord.py also has many features\nThe bot has its own github page on the creator"s user"s github\nYou can also help the bot do its job!',
                color=0xffffff)
            await interaction.response.send_message(embed=embed)
            await interaction.response.defer()
        except Exception as e:
            logging.error(f"Errno: on 'about' command failed, start again {e}")
    
    @discord.app_commands.command(name="help", description="command gives window with help by bot") 
    async def help(self, interaction: discord.Interaction) -> None:
        try:
            embed = discord.Embed(
                title=f'CE_bot help',
                description=f'/userinfo <member> - get member information/py <code> - runs python code and gives answer\n/clear <amount> - command to clear the chat\n/kick <member> <reason> - kicks the user from the server\n/ban <member> <reason> - bans the caller from the server\n/about - gives information about the bot/server\n/assignrole <member> <role> - Assigns a role to an assigner\n/removerole <member> <role> - Removes a role from an assigner',
                color=0xffffff)
            await interaction.response.send_message(embed=embed)
            await interaction.response.defer()
        except Exception as e:
            logging.error(f"Errno: on 'help' command failed, start again {e}")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(info(bot))
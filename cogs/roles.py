import discord
from discord.ext import commands

import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(filename="logs/ce_.log", level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class roles(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
            
    @discord.app_commands.command(name="assignrole", description="allows the user to assign a role") 
    @discord.app_commands.describe(member="user who needs the role")
    @discord.app_commands.describe(role="role to be given")
    async def assignrole(self, interaction: discord.Interaction, member: discord.Member, role: discord.Role) -> None:
        try:
            role_user = discord.utils.get(interaction.user.roles, name="Модератор")
            if member and role and role_user:
                await member.add_roles(role)
                embed = discord.Embed(
                    title=f'Role Granted',
                    description=f'You saw the role of {member.mention} now he is happier than ever',
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
            logging.error(f"Errno: on 'assignrole' command failed, start again {e}")

    @discord.app_commands.command(name="removerole", description="command that removes a role from a user") 
    @discord.app_commands.describe(member="who needs to take the role")
    @discord.app_commands.describe(role="role to be removed")
    async def removerole(self, interaction: discord.Interaction, member: discord.Member, role: discord.Role) -> None:
        try:
            role_user = discord.utils.get(interaction.user.roles, name="Модератор")
            if member and role and role_user:
                await member.remove_roles(role)
                embed = discord.Embed(
                    title=f'Role Removed',
                    description=f'You removed the role from {member.mention} now he is not happy',
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
            logging.error(f"Errno: on 'removerole' command failed, start again {e}")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(roles(bot))
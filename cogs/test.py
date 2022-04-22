import discord
from discord.commands import slash_command, Option
from discord.ui import InputText, Modal
from discord.ext import commands


class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

def setup(bot):
    bot.add_cog(test(bot))
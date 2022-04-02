import discord
from discord.commands import slash_command
from discord.ext import commands
from discord.utils import get

import setting


class enjoy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids = [setting.test_guild], description="유저가 한 말을 따라합니다.")
    async def 따라하기(self, ctx, 따라할말):
        if "@everyone" in 따라할말 or "@here" in 따라할말:
            await ctx.channel.send(embed=discord.Embed(title="`@everyone`이나 `@here`이 포함된 채팅은 따라하지 않습니다.",color=0xffdc16))
            return
        else:
            await ctx.respond(f"{따라할말}")

def setup(bot):
    bot.add_cog(enjoy(bot))
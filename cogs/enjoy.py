import discord
from discord.commands import slash_command, Option
from discord.ext import commands
from discord.utils import get
from random import randrange, randint

import setting


class enjoy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids = [setting.test_guild], description="유저가 한 말을 따라합니다.")
    async def 따라하기(self, ctx, 따라할말:Option(str,"봇이 따라할 말을 입력해주세요")):
        if "@everyone" in 따라할말 or "@here" in 따라할말:
            await ctx.channel.send(embed=discord.Embed(title="`@everyone`이나 `@here`이 포함된 채팅은 따라하지 않습니다.",color=0xffdc16))
            return
        else:
            await ctx.respond(f"{따라할말}")

    @slash_command(guild_ids = [setting.test_guild], description="주사위를 하나 던집니다.")
    async def 주사위(self, ctx):
        randomNum = randrange(1,7)
        dicebox = {1:":one:", 2:":two:", 3:":three:", 4:":four:", 5:":five:", 6:":six:"}
        dicenum = dicebox[randomNum]
        dice = discord.Embed(title="주사위를 던졌다", description=f':game_die: {dicenum}', color=0xffdc16)
        await ctx.respond(embed=dice)

    @slash_command(guild_ids = [setting.test_guild], description="1부터 100중 랜덤한 숫자 하나를 뽑습니다.")
    async def 숫자(self, ctx):
        randomNum = randint(1,100)
        card = discord.Embed(title="랜덤숫자 뽑기", description="­", color=0xffdc16)
        card.add_field(name=randomNum, value="­", inline=False)
        card.set_thumbnail(url="https://cdn.discordapp.com/attachments/955355332983521300/960471817112412220/pcc.png")
        await ctx.respond(embed=card)


def setup(bot):
    bot.add_cog(enjoy(bot))
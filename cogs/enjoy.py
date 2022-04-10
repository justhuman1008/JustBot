import discord
from discord.commands import slash_command, Option
from discord.ext import commands
from discord.utils import get
from random import randrange, randint
import math



class enjoy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="유저가 한 말을 따라합니다.")
    async def 따라하기(self, ctx, 따라할말:Option(str,"봇이 따라할 말을 입력해주세요")):
        if "@everyone" in 따라할말 or "@here" in 따라할말:
            await ctx.channel.send(embed=discord.Embed(title="`@everyone`이나 `@here`이 포함된 채팅은 따라하지 않습니다.",color=0xffdc16))
            return
        else:
            await ctx.respond(f"{따라할말}")


    @slash_command(description="주사위를 하나 던집니다.")
    async def 주사위(self, ctx):
        randomNum = randrange(1,7)
        dicebox = {1:":one:", 2:":two:", 3:":three:", 4:":four:", 5:":five:", 6:":six:"}
        dicenum = dicebox[randomNum]
        dice = discord.Embed(title="주사위를 던졌다", description=f':game_die: {dicenum}', color=0xffdc16)
        await ctx.respond(embed=dice)


    @slash_command(description="1부터 100중 랜덤한 숫자 하나를 뽑습니다.")
    async def 숫자(self, ctx):
        randomNum = randint(1,100)
        card = discord.Embed(title="랜덤숫자 뽑기", description="­", color=0xffdc16)
        card.add_field(name=randomNum, value="­", inline=False)
        card.set_thumbnail(url="https://cdn.discordapp.com/attachments/955355332983521300/960471817112412220/pcc.png")
        await ctx.respond(embed=card)


    @slash_command(description="입력한 수가 소수인지 확인합니다.")
    async def 소수(self, ctx, 수:Option(int,"소수인지 확인할 수를 입력해주세요.")):
        
        integers_prime = f"https://www.integers.co/questions-answers/is-{수}-a-prime-number.html"
        naverdic = f"https://terms.naver.com/entry.naver?docId=1113970&cid=40942&categoryId=32206"

        isprime = discord.Embed(title=f"{수}은 소수입니다.", description=f'[{수}이 왜 소수인가요?]({integers_prime})', color=0xffdc16)
        isprime.set_thumbnail(url="https://cdn.discordapp.com/attachments/955355332983521300/962232633234948126/mathmu.png")

        noprime = discord.Embed(title=f"{수}은 소수가 아닙니다.", description=f'[{수}이 왜 소수가 아닌가요?]({integers_prime})', color=0xffdc16)
        noprime.set_thumbnail(url="https://cdn.discordapp.com/attachments/955355332983521300/962232633234948126/mathmu.png")

        prime0 = discord.Embed(title=f'0은 소수가 아닙니다.', description=f"[소수 - 지식백과]({naverdic})", color=0xf8e71c)
        prime0.set_thumbnail(url="https://cdn.discordapp.com/attachments/955355332983521300/962232633234948126/mathmu.png")

        negative_num = discord.Embed(title=f'음수({수})는 소수가 아닙니다.', description=f"[소수 - 지식백과]({naverdic})", color=0xf8e71c)
        negative_num.set_thumbnail(url="https://cdn.discordapp.com/attachments/955355332983521300/962232633234948126/mathmu.png")

        if 수 == 0: # 0
            return await ctx.respond(embed=prime0)
        elif 수 < 0: # 음수
            return await ctx.respond(embed=negative_num)
        elif 수 == 1: # 1
            return await ctx.respond(embed=noprime)
        elif 수 in [2, 3, 5, 7]: # 2,3,5,7은 소수임
            return await ctx.respond(embed=isprime)
        elif 수 % 2 == 0: # 2의 약수는 소수아님
            return await ctx.respond(embed=noprime)
        elif 수 % 5 == 0: # 5의 약수는 소수아님
            return await ctx.respond(embed=isprime)
        elif 수 >= 1000000001:  # 소수 확인 제한(현재 10억)
            await ctx.respond(embed=discord.Embed(title=f'10억 이상의 수는 확인할 수 없습니다.', description=f'확인을 시도한 수 {수}', color=0xf8e71c))
            return
        a = 3
        while a <= math.sqrt(수):
            if 수 % a == 0:
                return await ctx.respond(embed=noprime)
            a = a + (2, 4)[a % 10 == 3]
        return await ctx.respond(embed=isprime)




def setup(bot):
    bot.add_cog(enjoy(bot))
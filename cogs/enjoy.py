import discord
from discord.commands import slash_command, Option
from discord.ext import commands
from discord.utils import get
from random import randrange, randint
import math



class enjoy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="버튼식 계산기를 시작합니다.")
    async def 계산기(self, ctx):
        BotName = self.bot.user.name
        CalcEMV = discord.Embed(title=f"{BotName} 계산기", description=f'```\n0' + ' '*30 + '\n```', color=0xffdc16)
        CalcEMV.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/962232633234948126/mathmu.png')

        def symbols_Button(btn_self):
            marker = ["+","-","*","/"]
            last = str(btn_self.values[len(btn_self.values)-1:])

            Plus = [a for a in btn_self.children if a.custom_id=="+"][0]
            Minus = [b for b in btn_self.children if b.custom_id=="-"][0]
            Multiply = [c for c in btn_self.children if c.custom_id=="*"][0]
            Divide = [d for d in btn_self.children if d.custom_id=="/"][0]
            Equals = [e for e in btn_self.children if e.custom_id=="="][0]

            symbols = [Plus, Minus, Multiply, Divide, Equals]
            if last in marker:
                for symbol in symbols:
                    symbol.disabled = True
                return btn_self

            elif not last in marker:
                for symbol in symbols:
                    symbol.disabled = False
                return btn_self

        def MakeEmbed(btn_self):
            if btn_self.values == "":
                btn_self.values = "0"
            des = f'{str(btn_self.values)}' + ' '*30

            button_Option = symbols_Button(btn_self)

            if len(des) >= 31:
                des = des[:31]
                des2 = ""
                if len(btn_self.values) == 30:
                    des2 = '\n\n 계산기 범위를 벗어났습니다. \n계산이 정확히 되지 않을 수 있습니다.'
            CalcEMV = discord.Embed(title=f"{BotName} 계산기", description='```\n'+des+'\n```'+des2, color=0xffdc16)
            CalcEMV.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/962232633234948126/mathmu.png')
            return CalcEMV, button_Option

        class CalcView(discord.ui.View):
            def __init__(self):
                self.values = ""
                super().__init__(timeout=None)

            @discord.ui.button(label="9", style=discord.ButtonStyle.gray, row=0)
            async def Nime(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values += "9"
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="8", style=discord.ButtonStyle.gray, row=0)
            async def Eight(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values += "8"
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="7", style=discord.ButtonStyle.gray, row=0)
            async def Seven(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values += "7"
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="+", style=discord.ButtonStyle.blurple, row=0, custom_id="+")
            async def Plus(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values += "+"
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="Exit", style=discord.ButtonStyle.red, row=0)
            async def Off(self, button: discord.ui.Button, interaction: discord.Interaction):
                await interaction.response.edit_message(view=None)

            @discord.ui.button(label="6", style=discord.ButtonStyle.gray, row=1)
            async def Six(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values += "6"
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="5", style=discord.ButtonStyle.gray, row=1)
            async def Five(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values += "5"
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="4", style=discord.ButtonStyle.gray, row=1)
            async def Four(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values += "4"
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="-", style=discord.ButtonStyle.blurple, row=1, custom_id="-")
            async def Minus(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values += "-"
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="C", style=discord.ButtonStyle.red, row=1, custom_id="C")
            async def C(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values = ""
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="3", style=discord.ButtonStyle.gray, row=2)
            async def Three(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values += "3"
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="2", style=discord.ButtonStyle.gray, row=2)
            async def Two(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values += "2"
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="1", style=discord.ButtonStyle.gray, row=2)
            async def One(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values += "1"
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="*", style=discord.ButtonStyle.blurple, row=2, custom_id="*")
            async def Multiply(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values += "*"
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="⌫", style=discord.ButtonStyle.red, row=2, custom_id="⌫")
            async def Delete(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values = self.values[:len(self.values)-1]
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="00", style=discord.ButtonStyle.gray, row=3)
            async def twoZero(self, button: discord.ui.Button, interaction: discord.Interaction):
                if not self.values == "":
                    self.values += "00"
                    CalcEMV, button_Option = MakeEmbed(self)
                    await interaction.response.edit_message(embed=CalcEMV,view=button_Option)
                else:
                    return

            @discord.ui.button(label="0", style=discord.ButtonStyle.gray, row=3)
            async def Zero(self, button: discord.ui.Button, interaction: discord.Interaction):
                if not self.values == "":
                    self.values += "0"
                    CalcEMV, button_Option = MakeEmbed(self)
                    await interaction.response.edit_message(embed=CalcEMV,view=button_Option)
                else:
                    return

            @discord.ui.button(label=".", style=discord.ButtonStyle.gray, row=3, custom_id=".")
            async def Dot(self, button: discord.ui.Button, interaction: discord.Interaction):
                if self.values == "":
                    self.values += "0."
                else:
                    self.values += "."
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="/", style=discord.ButtonStyle.blurple, row=3, custom_id="/")
            async def Divide(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values += "/"
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

            @discord.ui.button(label="=", style=discord.ButtonStyle.green, row=3, custom_id="=")
            async def Equals(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.values = str(eval(self.values))
                CalcEMV, button_Option = MakeEmbed(self)
                await interaction.response.edit_message(embed=CalcEMV,view=button_Option)

        await ctx.respond(embed=CalcEMV, view=CalcView())

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
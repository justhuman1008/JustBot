import discord
from discord.commands import Option
from discord.ext import tasks
import os
from itertools import cycle

from setting import test_guild, token, owner

bot = discord.Bot()


@bot.event # 봇 작동
async def on_ready():
    print("=========================")
    print("아래의 계정으로 로그인 : ")
    print(bot.user.name)
    print("연결에 성공했습니다.")
    print("=========================")

for filename in os.listdir('./cogs'): # Cogs 자동 로드(봇 작동시)
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename[:-3]}가 정상적으로 로드되었습니다.')


Status = cycle(['/help', 'Minecraft', '/help', '!help'])
@tasks.loop(seconds=10) # 상태메시지 자동 변경
async def change_status():
    await bot.change_presence(activity=discord.Game(next(Status)))


@bot.slash_command(guild_ids = [test_guild], description="봇 도움말 확인")
async def 도움말(ctx, 플러그인:Option(str,"다음 중 하나를 선택하세요.", choices=["서버관리", "검색","마인크래프트", "놀이"])=None):

    help = discord.Embed(title=f"{bot.user.name} 도움말", description=f"­", colour=0xffdc16)
    help.add_field(name=f"서버관리", value=f"`/도움말 서버관리`", inline=True)
    help.add_field(name=f"검색", value=f"`/도움말 검색`", inline=True)
    help.add_field(name=f"마인크래프트", value=f"`/도움말 마인크래프트`", inline=True)
    help.add_field(name=f"놀이", value=f"`/도움말 놀이`", inline=True)
    help.add_field(name=f"5", value=f"`/도움말 5`", inline=True)
    help.set_thumbnail(url=bot.user.display_avatar)

    serverhelp = discord.Embed(title=f"서버관리 도움말", description=f"­", colour=0xffdc16)
    serverhelp.add_field(name=f"/서버정보", value=f":small_blue_diamond:"+"이 서버에 대한 정보를 불러옵니다.", inline=False)
    serverhelp.add_field(name=f"/내정보", value=f":small_blue_diamond:"+"내 디스코드 정보를 불러옵니다.", inline=False)
    serverhelp.add_field(name=f"/청소 `<삭제수량>`", value=f":small_blue_diamond:"+"채널의 메시지를 대량으로 삭제합니다.", inline=False)
    serverhelp.add_field(name=f"/추방 `<유저멘션>`", value=f":small_blue_diamond:"+"멘션한 유저를 추방합니다.", inline=False)
    serverhelp.add_field(name=f"/차단 `<유저멘션>`", value=f":small_blue_diamond:"+"멘션한 유저를 차단합니다.", inline=False)
    serverhelp.add_field(name=f"/초대링크 `[횟수제한]`", value=f":small_blue_diamond:"+"이 서버의 초대링크를 생성합니다.", inline=False)
    serverhelp.add_field(name=f"/역할생성 `<역할명>`", value=f":small_blue_diamond:"+"서버에 새로운 역할을 생성합니다.", inline=False)
    serverhelp.add_field(name=f"/채널생성 `<채널명>`", value=f":small_blue_diamond:"+"서버에 새로운 텍스트 채널을 생성합니다.", inline=False)
    serverhelp.add_field(name=f"/통화방생성 `<채널명>`", value=f":small_blue_diamond:"+"서버에 새로운 음성 채널을 생성합니다.", inline=False)
    serverhelp.add_field(name=f"/카테고리생성 `<카테고리명>`", value=f":small_blue_diamond:"+"서버에 새로운 카테고리를 생성합니다.", inline=False)
    serverhelp.add_field(name=f"/슬로우모드 `<초>`", value=f":small_blue_diamond:"+"채널에 슬로우모드를 겁니다.", inline=False)
    serverhelp.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/955355811910139904/cust.png')

    searchhelp = discord.Embed(title=f"검색 도움말", description=f"­", colour=0xffdc16)
    searchhelp.add_field(name=f"/구글 `<검색내용>`", value=f":small_blue_diamond:"+"구글에 검색합니다.", inline=False)
    searchhelp.add_field(name=f"/네이버 `<검색내용>`", value=f":small_blue_diamond:"+"네이버에 검색합니다.", inline=False)
    searchhelp.add_field(name=f"/멜론차트", value=f":small_blue_diamond:"+"멜론 차트 TOP10을 불러옵니다.", inline=False)
    searchhelp.add_field(name=f"/날씨 `<지역명>`", value=f":small_blue_diamond:"+"해당 지역의 날씨를 불러옵니다.", inline=False)
    searchhelp.add_field(name=f"/한강수온", value=f":small_blue_diamond:"+"한강의 실시간 수온을 불러옵니다.", inline=False)
    searchhelp.add_field(name=f"/코로나", value=f":small_blue_diamond:"+"대한민국의 코로나19 현황을 불러옵니다.", inline=False)
    searchhelp.add_field(name=f"/번역 `<번역할 내용>`", value=f":small_blue_diamond:"+"메세지를 번역합니다. [5000자 제한]", inline=False)
    searchhelp.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/959761638217629696/pngegg.png')

    minecrafthelp = discord.Embed(title=f"마인크래프트 도움말", description=f"­", colour=0xffdc16)

    playthelp = discord.Embed(title=f"놀이 도움말", description=f"­", colour=0xffdc16)

    if 플러그인 == None:
        await ctx.respond(embed=help)
        return
    else:
        if 플러그인 == "서버관리":
            await ctx.respond(embed=serverhelp)
            return
        searchplug = ["검색","ㄱ검색","파싱"]
        if 플러그인 == "검색":
            await ctx.respond(embed=searchhelp)
            return
        minecraftplug = ["마인크래프트""마크"]
        if 플러그인 == "마인크래프트":
            await ctx.respond(embed=minecrafthelp)
            return
        if 플러그인 == "놀이":
            await ctx.respond(embed=playthelp)
            return


        else:
            noplugin = discord.Embed(title=f":exclamation: 플러그인이 없습니다.", description=f"`/도움말`로 플러그인을 확인해주세요.", colour=0xffdc16)
            await ctx.respond(embed=noplugin)


@bot.command(guild_ids = [test_guild], description="봇 레이턴시 확인")
async def ping(ctx):
    ping = discord.Embed(title="Pong!", description=f"딜레이: {round(bot.latency * 1000)}ms 초", colour=0xffdc16)
    await ctx.respond(embed=ping)


@bot.command(guild_ids = [test_guild], description=f"봇에 대한 정보를 출력합니다.")
async def 정보(ctx):
    botinfo = discord.Embed(title=bot.user.name, color=0xffdc16)
    botinfo.add_field(name="핑", value=f'`{round(bot.latency * 1000)}ms`', inline=True)
    botinfo.add_field(name='봇 접두사', value='`/{명령어}`', inline=True)
    botinfo.add_field(name="­", value="­", inline=True)
    botinfo.add_field(name="연결된 서버 수⠀⠀⠀", value=f'`{len(bot.guilds)}개 서버`', inline=True)
    botinfo.add_field(name="이용중인 유저 수", value=f'`{len(bot.users)}명`', inline=True)
    botinfo.add_field(name="­", value="­", inline=True)
    botinfo.add_field(name="개발 언어", value="Python [Pycord](https://docs.pycord.dev/en/master/)", inline=True)
    botinfo.add_field(name='GitHub', value='[Bot GitHub](https://github.com/justhuman1008/JustBot)', inline=True)
    botinfo.add_field(name="호스팅", value="[Heroku](https://heroku.com/)", inline=True)
    botinfo.add_field(name="소유자", value=f"{owner}", inline=False)
    botinfo.set_thumbnail(url=bot.user.display_avatar)
    await ctx.respond(embed=botinfo)


@bot.command(aliases=['hellothisisverification'], description="개발자확인용")#한국봇리스트 인증용
async def checkbotowner(ctx):
    await ctx.respond(owner+"v1")


'''
@bot.event
async def on_ready():
    ch = bot.get_channel(927913185766436885)
    await ch.purge(limit = 100)
    v = discord.ui.View()
    v.add_item(Vrb())
    await ch.send(view=v)
'''
bot.run(token)
import discord
from discord.commands import Option
from discord.ui import View
from os import listdir
from sys import exit

from setting import token, owner, guild
BOT_token = token

bot = discord.Bot()

if BOT_token == "":
    print("=========================")
    print("봇 계정 연결에 실패했습니다.")
    print("디스코드 봇의 토큰을 입력해주세요.")
    print("=========================")
    exit()


@bot.event # 봇 작동
async def on_ready():
    print("=========================")
    print("아래의 계정으로 로그인 : ")
    print(bot.user.name)
    print("연결에 성공했습니다.")
    print("=========================")
    await bot.change_presence(activity=discord.Game("/도움말"))

for filename in listdir('./cogs'): # Cogs 자동 로드(봇 작동시)
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename[:-3]}가 정상적으로 로드되었습니다.')



@bot.slash_command(description="봇 도움말 확인")
async def 도움말(ctx, 플러그인:Option(str,"다음 중 하나를 선택하세요.", choices=["서버관리", "검색", "놀이", "마인크래프트", "봇"])=None):

    help = discord.Embed(title=f"{bot.user.name} 도움말", description=f"­", colour=0xffdc16)
    help.add_field(name=f"서버관리", value=f"`/도움말 서버관리`", inline=True)
    help.add_field(name=f"검색", value=f"`/도움말 검색`", inline=True)
    help.add_field(name=f"놀이", value=f"`/도움말 놀이`", inline=True)
    help.add_field(name=f"마인크래프트", value=f"`/도움말 마인크래프트`", inline=True)
    help.add_field(name=f"봇", value=f"`/도움말 봇`", inline=True)
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
    searchhelp.add_field(name=f"/번역 `<번역할 내용>`", value=f":small_blue_diamond:"+"메세지를 번역합니다. [5000자 제한]", inline=False)
    searchhelp.add_field(name=f"/코로나", value=f":small_blue_diamond:"+"대한민국의 코로나19 현황을 불러옵니다.", inline=False)
    searchhelp.add_field(name=f"/날씨 `<지역명>`", value=f":small_blue_diamond:"+"해당 지역의 날씨를 불러옵니다.", inline=False)
    searchhelp.add_field(name=f"/단축링크 `<URL>`", value=f":small_blue_diamond:"+"입력한 링크를 단축합니다.", inline=False)
    searchhelp.add_field(name=f"/위키실검", value=f":small_blue_diamond:"+"나무위키의 실시간 검색어를 불러옵니다.", inline=False)
    searchhelp.add_field(name=f"/멜론차트", value=f":small_blue_diamond:"+"멜론 차트 TOP10을 불러옵니다.", inline=False)
    searchhelp.add_field(name=f"/한강수온", value=f":small_blue_diamond:"+"한강의 실시간 수온을 불러옵니다.", inline=False)
    searchhelp.add_field(name=f"/롤티어 `<닉네임>`", value=f":small_blue_diamond:"+"유저의 리그오브레전드 티어를 불러옵니다.", inline=False)
    searchhelp.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/959761638217629696/pngegg.png')

    playhelp = discord.Embed(title=f"놀이 도움말", description=f"­", colour=0xffdc16)
    playhelp.add_field(name=f"/계산기", value=f":small_blue_diamond:"+"버튼식 계산기를 시작합니다.", inline=False)
    playhelp.add_field(name=f"/따라하기 `<따라할말>`", value=f":small_blue_diamond:"+"유저가 한 말을 따라합니다.", inline=False)
    playhelp.add_field(name=f"/주사위", value=f":small_blue_diamond:"+"주사위를 하나 던집니다.", inline=False)    
    playhelp.add_field(name=f"/숫자", value=f":small_blue_diamond:"+"1부터 100중 랜덤한 숫자 하나를 뽑습니다.", inline=False)
    playhelp.add_field(name=f"/소수 `<수>`", value=f":small_blue_diamond:"+"입력한 수가 소수인지 확인합니다.", inline=False)
    playhelp.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/960057531512799242/lego.png')

    minecrafthelp = discord.Embed(title=f"마인크래프트 도움말", description=f"Java Edition 1.18.2 기준", colour=0xffdc16)
    minecrafthelp.add_field(name=f"/uuid `<닉네임>`", value=f":small_blue_diamond:"+"유저의 마인크래프트 UUID를 검색합니다.", inline=False)
    minecrafthelp.add_field(name=f"/스킨 `<닉네임>`", value=f":small_blue_diamond:"+"유저의 마인크래프트 스킨을 검색합니다.", inline=False)
    minecrafthelp.add_field(name=f"/서버상태 `<서버주소>`", value=f":small_blue_diamond:"+"마인크래프트 서버의 상태를 확인합니다.", inline=False)
    minecrafthelp.add_field(name=f"/발전과제 `<발전과제트리>`", value=f":small_blue_diamond:"+"마인크래프트 발전과제 목록을 확인합니다.", inline=False)
    minecrafthelp.add_field(name=f"/마크사양 `<권장,최소>`", value=f":small_blue_diamond:"+"마인크래프트 사양을 확인합니다.", inline=False)
    minecrafthelp.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/960085353404964884/minecraft.png')

    bothelp = discord.Embed(title=f"봇 도움말", description=f"­", colour=0xffdc16)   
    bothelp.add_field(name=f"/ping", value=f":small_blue_diamond:"+"봇 레이턴시 확인", inline=False)
    bothelp.add_field(name=f"/정보", value=f":small_blue_diamond:"+"봇에 대한 정보를 출력합니다.", inline=False)
    bothelp.add_field(name=f"/invite", value=f":small_blue_diamond:"+"봇 초대링크", inline=False)
    bothelp.add_field(name=f"/도움말", value=f":small_blue_diamond:"+"봇 도움말 확인", inline=False)
    bothelp.add_field(name=f"/명령어", value=f":small_blue_diamond:"+"봇에서 사용가능한 모든 명령어를 출력합니다.", inline=False)
    bothelp.set_thumbnail(url=bot.user.display_avatar)

    if 플러그인 == None:
        await ctx.respond(embed=help)
        return
    else:
        if 플러그인 == "서버관리":
            await ctx.respond(embed=serverhelp)
            return
        if 플러그인 == "검색":
            await ctx.respond(embed=searchhelp)
            return
        if 플러그인 == "놀이":
            await ctx.respond(embed=playhelp)
            return
        if 플러그인 == "마인크래프트":
            await ctx.respond(embed=minecrafthelp)
            return
        if 플러그인 == "봇":
            await ctx.respond(embed=bothelp)
            return

        else:
            noplugin = discord.Embed(title=f":exclamation: 플러그인이 없습니다.", description=f"`/도움말`로 플러그인을 확인해주세요.", colour=0xffdc16)
            await ctx.respond(embed=noplugin)


@bot.slash_command(description="봇에서 사용가능한 모든 명령어를 출력합니다.")
async def 명령어(ctx):
    cmdlist = discord.Embed(title=bot.user.name, color=0xffdc16)
    cmdlist.add_field(name="서버관리", value='`/서버정보` `/내정보` `/청소` `/추방` `/차단` `/초대링크` `/역할생성` `/채널생성` `/통화방생성` `/카테고리생성` `/슬로우모드`', inline=False)
    cmdlist.add_field(name='검색', value='`/구글` `/네이버` `/번역` `/코로나` `/날씨` `/단축링크` `/위키실검` `/멜론차트` `/한강수온` `/롤티어`', inline=False)
    cmdlist.add_field(name="놀이", value='`/계산기` `/따라하기` `/주사위` `/숫자` `/소수`', inline=False)
    cmdlist.add_field(name="마인크래프트", value='`/uuid` `/스킨` `/서버상태` `/발전과제` `/마크사양`', inline=False)
    cmdlist.add_field(name="봇", value="`/ping` `정보` `/invite` `/도움말` `/명령어`", inline=False)
    cmdlist.set_thumbnail(url=bot.user.display_avatar)
    await ctx.respond(embed=cmdlist)


@bot.command(description="봇 레이턴시 확인")
async def ping(ctx):
    ping = discord.Embed(title="Pong!", description=f"딜레이: {round(bot.latency * 1000)}ms 초", colour=0xffdc16)
    await ctx.respond(embed=ping)


@bot.command(description=f"봇에 대한 정보를 출력합니다.")
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

@bot.command(description=f"봇 초대링크")
async def invite(ctx):
    invitelink = f"https://discord.com/oauth2/authorize?client_id={bot.application_id}&permissions=137715076183&scope=bot%20applications.commands"

    invite = discord.Embed(title=f"{bot.user.name} 초대하기", description=f"[봇 초대하기]({invitelink})", colour=0xffdc16)
    invite.set_thumbnail(url=bot.user.display_avatar)

    button = discord.ui.Button(label="봇 초대하기", url=invitelink, emoji="✉️")
    view = View()
    view.add_item(button)

    await ctx.respond(embed=invite,view=view)

bot.run(BOT_token)
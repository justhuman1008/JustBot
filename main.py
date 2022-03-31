import discord
from discord.commands import Option
import os

from setting import test_guild, token

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


@bot.slash_command(guild_ids = [test_guild], description="봇 레이턴시 확인")
async def ping(ctx):
    ping = discord.Embed(title="Pong!", description=f"딜레이: {bot.latency} 초", colour=0xffdc16)
    await ctx.respond(embed=ping)


@bot.slash_command(guild_ids = [test_guild], description="봇 도움말 확인")
async def 도움말(ctx, 플러그인:Option(str,"다음 중 하나를 선택하세요.", choices=["서버관리", "검색","마인크래프트"])=None):

    help = discord.Embed(title=f"{bot.user.name} 도움말", description=f"­", colour=0xffdc16)
    help.add_field(name=f"서버관리", value=f"`/도움말 서버관리`", inline=True)
    help.add_field(name=f"검색", value=f"`/도움말 검색`", inline=True)
    help.add_field(name=f"3", value=f"`/도움말 3`", inline=True)
    help.add_field(name=f"4", value=f"`/도움말 4`", inline=True)
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

    minecrafthelp = discord.Embed(title=f"마인크래프트 도움말", description=f"­", colour=0xffdc16)

    if 플러그인 == None:
        await ctx.respond(embed=help)
        return
    else:
        guildplug = ["서버관리","ㅅ서버관리","섭버관리"]
        if 플러그인 in guildplug:
            await ctx.respond(embed=serverhelp)
            return
        searchplug = ["검색","ㄱ검색","파싱"]
        if 플러그인 in searchplug:
            await ctx.respond(embed=searchhelp)
            return
        minecraftplug = ["마인크래프트","ㅁ마인크래프트","마크","ㅁ마크"]
        if 플러그인 in minecraftplug:
            await ctx.respond(embed=minecrafthelp)
            return



        else:
            noplugin = discord.Embed(title=f":exclamation: 플러그인이 없습니다.", description=f"`/도움말`로 플러그인을 확인해주세요.", colour=0xffdc16)
            await ctx.respond(embed=noplugin)




bot.run(token)
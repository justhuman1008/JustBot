import discord
from discord.commands import slash_command, Option
from discord.ext import commands
import requests

import setting


class ranking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="유저의 롤 티어를 불러옵니다.")
    async def 롤티어(self, ctx, 닉네임:Option(str,"롤 티어를 검색할 유저의 닉네임을 입력해주세요")):
        riotkey = setting.RiotAPIKey

        summoner_v4 = requests.get(f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{닉네임}?api_key={riotkey}").json()
        account_name = summoner_v4["name"]
        account_id = summoner_v4["accountId"]
        summoner_id = summoner_v4["id"]
        summoner_level = summoner_v4["summonerLevel"]

        league_v4 = requests.get(f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key={riotkey}").json()
        account_name_url = account_id.replace(" ","%20")
        try:
            if league_v4[0]['queueType'] == 'RANKED_SOLO_5x5':
                Solo_rank = league_v4[0]
                Free_rank = league_v4[1]
            elif league_v4[0]['queueType'] == 'RANKED_FLEX_SR':
                Solo_rank = league_v4[1]
                Free_rank = league_v4[0]

            Solo_win = Solo_rank['wins']
            Solo_lose = Solo_rank['losses']
            Free_win = Free_rank['wins']
            Free_lose = Free_rank['losses']
            lolSF = discord.Embed(title=f"{account_name}님의 리그 오브 레전드 티어", description=f'[op.gg 바로가기](https://www.op.gg/summoners/kr/{account_name_url})', color=0xffdc16)
            lolSF.add_field(name=f":star: 솔로랭크: {Solo_rank['tier']} {Solo_rank['rank']}",value=f"플레이: {Solo_win+Solo_lose}전", inline=False)
            lolSF.add_field(name='승률', value=f"{round((Solo_win/(Solo_win+Solo_lose)*100))}% ({Solo_win}승 {Solo_lose}패)", inline=True)
            lolSF.add_field(name='LP', value=f"{Solo_rank['leaguePoints']}", inline=True)
            lolSF.add_field(name=f":star: 자유랭크: {Free_rank['tier']} {Free_rank['rank']}",value=f"플레이: {Free_win+Free_lose}전", inline=False)
            lolSF.add_field(name='승률', value=f"{round((Free_win/(Free_win+Free_lose)*100))}% ({Free_win}승 {Free_lose}패)", inline=True)
            lolSF.add_field(name='LP', value=f"{Free_rank['leaguePoints']}", inline=True)
            lolSF
            lolSF.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/964471258093846548/lol_icon.png')

            await ctx.respond(embed=lolSF)
            return

        except:
            if league_v4[0]['queueType'] == 'RANKED_SOLO_5x5':
                rank_name = "솔로랭크"
                rank = league_v4[0]
                win = rank['wins']
                lose = rank['losses']

            else:
                rank_name = "자유랭크"
                rank = league_v4[0]
                win = Free_rank['wins']
                lose = Free_rank['losses']

            lol1 = discord.Embed(title=f"{account_name}님의 리그 오브 레전드 티어", description=f'[op.gg 바로가기](https://www.op.gg/summoners/kr/{account_name_url})', color=0xffdc16)
            lol1.add_field(name=f"{rank_name}: {rank['tier']} {rank['rank']}",value="­", inline=False)
            lol1.add_field(name='플레이 횟수', value=f"{win+lose}전", inline=True)
            lol1.add_field(name='승률', value=f"{round((win/(win+lose)*100))}% ({win}승 {lose}패)", inline=True)
            lol1.add_field(name='LP', value=f"{rank['leaguePoints']}", inline=True)
            lol1.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/964471258093846548/lol_icon.png')
            await ctx.respond(embed=lol1)
            return

def setup(bot):
    bot.add_cog(ranking(bot))
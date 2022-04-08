import discord
from discord.commands import slash_command, Option
from discord.ext import commands
import requests

import setting


class ranking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids = [setting.test_guild], description="유저의 롤 티어를 불러옵니다.")
    async def 롤티어(self, ctx, 닉네임:Option(str,"롤 티어를 검색할 유저의 닉네임을 입력해주세요")):
        try:
            account_idreq = requests.get(f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{닉네임}?api_key={setting.RiotAPIKey}")
            account_id = account_idreq.json()["accountId"]
            summoner_id = account_idreq.json()["id"]

            champion_json = requests.get("https://ddragon.leagueoflegends.com/cdn/12.6.1/data/ko_KR/champion.json").json()["data"]
            champ_dict = {}
            for champ in champion_json:
                row = champion_json[champ]
                champ_dict[row["key"]] = row["name"]

            lolTier = discord.Embed(title=f"{닉네임}님의 티어", colour=0xffdc16)
            lolTier.add_field(name=f"솔로 ", value=f"ㅁ", inline=True)
            lolTier.add_field(name=f"자유 5:5", value=f"ㅁ", inline=True)
            lolTier.add_field(name=f"주 챔피언", value=f"ㅁ", inline=True)
            lolTier.add_field(name=f"ㅁ", value=f"ㅁ", inline=True)
            await ctx.respond(f"소환사ID: {summoner_id}\n계정ID: {account_id}")

        except:
            weathererror = discord.Embed(title= "롤 티어 불러오기 실패", color=0xffdc16)
            weathererror.add_field(name=f"닉네임이 `{닉네임}`이(가) 맞는지 확인해주세요.", value=f"­")
            await ctx.respond(embed=weathererror)


'''
static_champ_list = requests.get(
    "http://ddragon.leagueoflegends.com/cdn/11.4.1/data/ko_KR/champion.json"
).json()
champ_dict = {}
# 모든 챔피언의 ID에 대치되는 이름을 champ_dict에 저장
for champ in static_champ_list["data"]:
    row = static_champ_list["data"][champ]
    champ_dict[row["key"]] = row["name"]
'''

def setup(bot):
    bot.add_cog(ranking(bot))
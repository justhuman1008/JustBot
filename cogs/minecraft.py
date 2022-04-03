import discord
from discord.commands import slash_command
from discord.ext import commands
from discord.utils import get
import requests

import setting

def findUUID(nickname):        
    try:
        mojangAPI = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{nickname}").json()
        uuid = mojangAPI["id"]
        name = mojangAPI["name"]
        return name, uuid
    except :
        uuid = 'Not Found'
        name = 'Not Found'
        return name, uuid

class minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids = [setting.test_guild], description="유저의 마인크래프트 UUID를 검색합니다.")
    async def uuid(self, ctx, 닉네임):
        name, uuid = findUUID(닉네임)
        if name == 'Not Found':
            NfoundUUID = discord.Embed(title= "UUID 로드 실패", color=0xffdc16, description="아래의 내용을 확인해주세요")
            NfoundUUID.add_field(name="­", value=f"닉네임이 `{닉네임}`이(가) 맞는지 확인해주세요.", inline=False)
            NfoundUUID.add_field(name="­", value=f"[Mojang API](https://api.mojang.com/users/profiles/minecraft/{닉네임})가 작동하고 있는지 확인해주세요.", inline=False)
            await ctx.respond(embed=NfoundUUID)
            return
        else:
            foundUUID = discord.Embed(title= f"{name}의 UUID", color=0xffdc16, description=f"{uuid}")
            foundUUID.set_thumbnail(url=f"https://crafatar.com/avatars/{uuid}.png?overlay")
            await ctx.respond(embed=foundUUID)

    @slash_command(guild_ids = [setting.test_guild], description="유저의 마인크래프트 스킨을 검색합니다.")
    async def 스킨(self, ctx, 닉네임):
        name, uuid = findUUID(닉네임)
        if name == 'Not Found':
            NfoundUUID = discord.Embed(title= "스킨 로드 실패", color=0xffdc16, description="아래의 내용을 확인해주세요")
            NfoundUUID.add_field(name="­", value=f"닉네임이 `{닉네임}`이(가) 맞는지 확인해주세요.", inline=False)
            NfoundUUID.add_field(name="­", value=f"[Mojang API](https://api.mojang.com/users/profiles/minecraft/{닉네임})가 작동하고 있는지 확인해주세요.", inline=False)
            await ctx.respond(embed=NfoundUUID)
            return
        else:
            foundSKIN = discord.Embed(title=f"{name}님의 스킨", description=f"[스킨 다운로드](https://minecraftskinstealer.com/api/v1/skin/download/skin/{닉네임})", color=0xffdc16)
            foundSKIN.set_image(url=f"https://crafatar.com/renders/body/{uuid}.png?overlay")
            await ctx.respond(embed=foundSKIN)




def setup(bot):
    bot.add_cog(minecraft(bot))
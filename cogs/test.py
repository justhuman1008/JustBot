import discord
import asyncio
from discord.commands import slash_command
from discord.ext import commands
from discord.utils import get
from bs4 import BeautifulSoup
import requests
import urllib
from urllib.request import urlopen, Request
import furl
import json
from datetime import date, timedelta
import time

import setting


class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids = [setting.test_guild], description="버튼을 생성합니다.")
    async def 버튼(self, ctx):
        class Button(discord.ui.View):
            @discord.ui.button(label="primary", style=discord.ButtonStyle.primary)
            async def primary(self, button: discord.ui.Button, interaction: discord.Interaction):
                await ctx.respond(f"<@!{interaction.user.id}> 님이 primary 버튼을 눌렀어요!")

            @discord.ui.button(label="green", style=discord.ButtonStyle.green)
            async def green(self, button: discord.ui.Button, interaction: discord.Interaction):
                await ctx.respond(f"<@!{interaction.user.id}> 님이 green 버튼을 눌렀어요!")

            @discord.ui.button(label="gray", style=discord.ButtonStyle.gray)
            async def gray(self, button: discord.ui.Button, interaction: discord.Interaction):
                await ctx.respond(f"<@!{interaction.user.id}> 님이 gray 버튼을 눌렀어요!")

            @discord.ui.button(label="primary", style=discord.ButtonStyle.primary)
            async def primary2(self, button: discord.ui.Button, interaction: discord.Interaction):
                await ctx.respond(f"<@!{interaction.user.id}> 님이 primary2 버튼을 눌렀어요!")

            @discord.ui.button(label="green", style=discord.ButtonStyle.green)
            async def green2(self, button: discord.ui.Button, interaction: discord.Interaction):
                await ctx.respond(f"<@!{interaction.user.id}> 님이 green2 버튼을 눌렀어요!")

            @discord.ui.button(label="gray", style=discord.ButtonStyle.gray)
            async def gray2(self, button: discord.ui.Button, interaction: discord.Interaction):
                await ctx.respond(f"<@!{interaction.user.id}> 님이 gray2 버튼을 눌렀어요!")

        await ctx.respond("버튼을 누르세요.", view=Button())  

    @slash_command(guild_ids = [setting.test_guild], description="드래그드랍을 생성합니다.1")
    async def 드랍다운(self, ctx):
        class selector(discord.ui.View):
            @discord.ui.select(placeholder="사용할 검색엔진을 선택하세요",min_values=1,max_values=1,options=[
                    discord.SelectOption(label="구글",description="세계 1위 검색엔진"),
                    discord.SelectOption(label="네이버",description="대한민국 1위 검색엔진"),
                    discord.SelectOption(label="다음",description="카카오에서 운영하는 검색엔진"),
                    discord.SelectOption(label="Bing",description="세계 2위 검색엔진"),
            ])
            async def dropreturn(self, select, interaction: discord.Interaction):
                if select.values[0] == "한국어":
                    await interaction.response.send_message("안녕")
                if select.values[0] == "영어":
                    await interaction.response.send_message("안녕2")
                if select.values[0] == "일본어":
                    await interaction.response.send_message("안녕3")
                if select.values[0] == "중국어 간체":
                    await interaction.response.send_message("안녕4")
                if select.values[0] == "중국어 번체":
                    await interaction.response.send_message("안녕5")
                #await dropdown.edit_original_message(content = select.values[0])
        choice = selector(timeout=30)
        dropdown = await ctx.respond("검색에 사용할 검색엔진을 선택하세요", view=choice)


def setup(bot):
    bot.add_cog(test(bot))
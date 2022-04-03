from discord.ext import commands
import requests

import setting


champion_json = requests.get("https://ddragon.leagueoflegends.com/cdn/12.6.1/data/ko_KR/champion.json").json()

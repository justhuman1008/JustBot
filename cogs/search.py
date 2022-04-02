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

import setting


class search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids = [setting.test_guild], description="구글에 검색합니다.")
    async def 구글(self, ctx, 검색내용):
        url = 'https://www.google.com/search?q='+검색내용

        google = discord.Embed(title="구글 검색", description=f"[{검색내용} - Google 검색]({url})", color=0xffdc16)
        google.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/955382311103389706/google-logos-2018-5.png')
        await ctx.respond(embed=google)


    @slash_command(guild_ids = [setting.test_guild], description="네이버에 검색합니다.")
    async def 네이버(self, ctx, 검색내용):
        url = 'https://search.naver.com/search.naver?query='+검색내용

        naver = discord.Embed(title="네이버 검색", description=f"[{검색내용} : 네이버 통합 검색]({url})", color=0xffdc16)
        naver.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/955382388748324884/nalogo.png')
        await ctx.respond(embed=naver)


    @slash_command(guild_ids = [setting.test_guild], description="멜론 차트 TOP10을 불러옵니다.")
    async def 멜론차트(self, ctx):
        melon = discord.Embed(
            title="멜론 음악차트", description="[멜론차트 바로가기](https://www.melon.com/chart/index.htm)", color=0xffdc16)
        targetSite = 'https://www.melon.com/chart/index.htm'

        header = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        melonrqRetry = requests.get(targetSite, headers=header)
        melonht = melonrqRetry.text
        melonsp = BeautifulSoup(melonht, 'html.parser')
        artists = melonsp.findAll('span', {'class': 'checkEllipsis'})
        titles = melonsp.findAll('div', {'class': 'ellipsis rank01'})
        for i in range(10):
            artist = artists[i].text.strip()
            title = titles[i].text.strip()
            melon.add_field(name="{0:3d}위 : {1}".format(i + 1, title), value='{0} - {1}'.format(artist, title), inline=False)
            melon.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/955382742550466600/1.png')
        await ctx.respond(embed=melon)


    @slash_command(guild_ids = [setting.test_guild], description="해당 지역의 날씨를 불러옵니다.")
    async def 날씨(self, ctx, 지역명):
        try:
            enc_location = urllib.parse.quote(지역명+'날씨')
            hdr = {'User-Agent': 'Mozilla/5.0'}
            url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
            req = Request(url, headers=hdr)
            html = urllib.request.urlopen(req)
            bsObj = BeautifulSoup(html, "html.parser")

            area = bsObj.find('h2', {'class': 'title'}) # 지역명
            area = area.text

            Temp = bsObj.find('div', {'class': 'temperature_text'}).get_text() # 현재 온도
            find_num = Temp.find('도')+1
            Temp = Temp[find_num:]

            MXLW_Temp = bsObj.find('div', {'class': 'cell_temperature'}).get_text() # 오늘 최저/최고 온도
            MXLW_Temp = MXLW_Temp.replace("기온","기온: ")

            Cast = bsObj.find('p', {'class': 'summary'}).get_text() # 기상정보 요약
            Cast = Cast.replace("기온","기온: ")
            Cast = Cast.replace("요","요 / ")
            if Cast.find('높아요') > -1:
                Cast = Cast.replace('높아요', '낮아요')
            elif Cast.find('낮아요') > -1:
                rainper = Cast.replace('낮아요', '높아요')

            rainper = bsObj.select('dd', {'class': 'desc'})[0].get_text() # 강수확률
            vapor = bsObj.select('dd', {'class': 'desc'})[1].get_text() # 습도

            weather = discord.Embed(title=area+ ' 날씨 정보', description=f'[네이버 날씨 바로가기]({url})', color=0xffdc16)
            weather.add_field(name="현재 상태",value=Cast)
            weather.add_field(name='현재 온도', value=Temp+'C', inline=False)
            weather.add_field(name='오늘 최저/최고 기온', value=MXLW_Temp, inline=False)
            weather.add_field(name='현재 강수확률', value=rainper, inline=False)
            weather.add_field(name='현재 습도', value=vapor, inline=False)
            weather.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/955382933546479636/pngwing.com.png')

            if Cast.find("맑음") > -1:
                weather.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/955383039800774686/01.png')
            elif Cast.find("흐림") > -1:
                weather.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/955383169060855830/07.png')
            elif Cast.find("구름많음") > -1:
                weather.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/955383269568946196/05.png')
            elif Cast.find("비") > -1:
                weather.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/955383414821888000/09.png')

            await ctx.respond(embed=weather)
        except:
            weathererror = discord.Embed(title= "날씨 불러오기 실패", color=0xffdc16, description="아래의 내용을 확인해주세요")
            weathererror.add_field(name=f"지역명이 `{지역명}`이(가) 맞는지 확인해주세요.", value=f"지역단위가 작다면(ex (읍,면,동)) `속한 지자체를 같이 입력`해보세요", inline=False)
            weathererror.add_field(name="­네이버 검색이 작동하고 있는지 확인해주세요.", value="­", inline=False)
            await ctx.respond(embed=weathererror)


    @slash_command(guild_ids = [setting.test_guild], description="한강의 실시간 수온을 불러옵니다.")
    async def 한강수온(self, ctx):
        req = Request("http://hangang.dkserver.wo.tc/")
        webpage = urlopen(req).read()
        output = json.loads(webpage)
        temp = output['temp']
        time = output['time']
        if temp == "운전정지":
            tempstop = discord.Embed(title=f"한강 수온을 불러올 수 없습니다.", description=f"API가 작동정지된 상태입니다.", color=0xffdc16)
            await ctx.respond(embed=tempstop)
            return
        hanriver = discord.Embed(title=f"현재 한강 수온은 {temp}°C", description=f"들어가기 딱 좋은 온도", color=0xffdc16)
        hanriver.set_footer(text=f"측정 시각: {time}")
        hanriver.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/955383697488625674/gksrks.jpg')
        await ctx.respond(embed=hanriver)

    @slash_command(guild_ids = [setting.test_guild], description="대한민국의 코로나19 현황을 불러옵니다.")
    async def 코로나(self, ctx):
        servicekey = setting.covid19APIkey
        if servicekey == "":
            await ctx.respond(embed=discord.Embed(title=f"해당 명령어는 사용 할 수 없습니다.", description=f"봇 관리자에게 문의하세요.", color=0xf8e71c))
            return
        today = date.today().strftime('%Y%m%d')
        yesterday = date.today() - timedelta(1)
        yesterday = yesterday.strftime('%Y%m%d')

        APIurl = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
        url = f"{APIurl}?ServiceKey={servicekey}&numOfRows=2&pageNo=1&startCreateDt={yesterday}&endCreateDt={today}"

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        today_decideCnt = soup.select('items > item > decideCnt')[0].text # 오늘 누적 확진
        today_deathCnt = soup.select('items > item > deathcnt')[0].text # 오늘 누적 사망
        today_createDt = soup.select('items > item > createdt')[0].text # 업데이트 일시
        yesterday_decideCnt = soup.select('items > item > decideCnt')[1].text # 어제 누적 확진
        yesterday_deathCnt = soup.select('items > item > deathcnt')[1].text # 어제 누적 사망

        new_decide = format(int(today_decideCnt) - int(yesterday_decideCnt), ',') #신규 확진 계산
        new_dead = format(int(today_deathCnt) - int(yesterday_deathCnt)) #신규 사망 계산
        critical = round(int(today_deathCnt)/int(today_decideCnt)*100,2)
        today_decideCnt = format(int(today_decideCnt), ',')
        today_deathCnt = format(int(today_deathCnt), ',')

        covid19 = discord.Embed(title=f"코로나19 국내 현황", description=f"­", colour=0xffdc16)
        covid19.add_field(name=f"확진", value=f"{today_decideCnt}명\n(+{new_decide})⠀⠀⠀⠀⠀", inline=True)
        covid19.add_field(name=f"사망", value=f"{today_deathCnt}명\n(+{new_dead})⠀⠀⠀⠀", inline=True)
        covid19.add_field(name=f"치사율", value=f"{critical}%⠀⠀⠀", inline=True)
        covid19.add_field(name=f"코로나19 보도자료", value=f"[http://ncov.mohw.go.kr](http://ncov.mohw.go.kr/tcmBoardList.do)", inline=False)
        covid19.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/955649522753749022/af275a5f9980be9e.png')
        await ctx.respond(embed=covid19)


    @slash_command(guild_ids = [setting.test_guild], description="메세지를 번역합니다. [5000자 제한]")
    async def 번역(self, ctx, 번역할내용):
        languagebox = {"ko":"한국어", "en":"영어", "ja":"일본어", "zh-CN":"중국어 간체", "zh-TW":"중국어 번체", "vi":"베트남어", "id":"인도네사아어", "th":"태국어", "de":"독일어", "ru":"러시아어", "es":"스페인어", "it":"이탈리아어", "fr":"프랑스어"}
        unlanguagebox = { y:x for x,y in languagebox.items()}

        client_id = setting.NaverAPIID
        client_secret = setting.NaverAPIPW

        class selector(discord.ui.View):
            @discord.ui.select(placeholder="번역될 언어를 선택하세요",min_values=1,max_values=1,options=[
                    discord.SelectOption(label="한국어",description="한국어",emoji="🇰🇷"),
                    discord.SelectOption(label="영어",description="English",emoji="🇬🇧"),
                    discord.SelectOption(label="일본어",description="日本語",emoji="🇯🇵"),
                    discord.SelectOption(label="중국어 간체",description="中国人",emoji="🇨🇳"),
                    discord.SelectOption(label="중국어 번체",description="中國人",emoji="🇹🇼"),
                    discord.SelectOption(label="독일어",description="Deutsch",emoji="🇩🇪"),
                    discord.SelectOption(label="프랑스어",description="불어 | Français",emoji="🇫🇷"),
                    discord.SelectOption(label="러시아어",description="Русский",emoji="🇷🇺"),
                    discord.SelectOption(label="스페인어",description="에스파냐어 | español",emoji="🇪🇸"),
                    discord.SelectOption(label="이탈리아어",description="Italiano",emoji="🇮🇹"),
                    discord.SelectOption(label="베트남어",description="Tiếng Việt",emoji="🇻🇳"),
                    discord.SelectOption(label="인도네사아어",description="Bahasa Indonesia",emoji="🇮🇩"),
                    discord.SelectOption(label="태국어",description="ภาษาไทย",emoji="🇹🇭")
            ])

            async def dropreturn(self, select, interaction: discord.Interaction):
                await dropdown.edit_original_message(content=f"{select.values[0]}로 번역합니다.",view=None)
                beforelang = select.values[0]
                after_langcode = unlanguagebox[select.values[0]]

                Text = urllib.parse.quote(번역할내용)

                # 언어 감지
                data = "query=" + Text
                url = "https://openapi.naver.com/v1/papago/detectLangs"
                request = urllib.request.Request(url)
                request.add_header("X-Naver-Client-Id",client_id)
                request.add_header("X-Naver-Client-Secret",client_secret)
                response = urllib.request.urlopen(request, data=data.encode("utf-8"))
                rescode = response.getcode()
                if(rescode==200):
                    response_body1 = response.read()
                    res1 = json.loads(response_body1.decode('utf-8'))
                    before_langcode = res1['langCode']
                beforelang = languagebox[before_langcode]
                afterlang = languagebox[after_langcode]

                if beforelang == afterlang:
                    samelang = discord.Embed(title=f"동일한 언어가 선택되었습니다.", description=f"{번역할내용}은(는) {beforelang}로 {번역할내용}(...)입니다.", colour=0xffdc16)
                    await dropdown.edit_original_message(embed=samelang,content=None)
                    return

        
                data = f"source={before_langcode}&target={after_langcode}&text=" + Text
                url = "https://openapi.naver.com/v1/papago/n2mt"
                request = urllib.request.Request(url)
                request.add_header("X-Naver-Client-Id",client_id)
                request.add_header("X-Naver-Client-Secret",client_secret)
                response = urllib.request.urlopen(request, data=data.encode("utf-8"))
                rescode = response.getcode()
                if(rescode==200):
                    response_body2 = response.read()
                    res2 = json.loads(response_body2.decode('utf-8'))
                    after = res2['message']['result']['translatedText']

                    papago = discord.Embed(title=f"번역기", description=f"­", colour=0xffdc16)
                    papago.add_field(name=f"{beforelang}", value=f"{번역할내용}", inline=False)
                    papago.add_field(name=f"{afterlang}", value=f"{after}", inline=False)
                    papago.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/958683584284229672/papagonobg.png')
                    await dropdown.edit_original_message(embed=papago,content=None)
                else:
                    print("Error Code:" + rescode)


        dropdown = await ctx.respond("입력한 내용이 번역될 언어를 선택하세요.", view=selector())


def setup(bot):
    bot.add_cog(search(bot))
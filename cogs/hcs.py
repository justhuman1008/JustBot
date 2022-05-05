import discord
from discord.commands import slash_command, Option
from discord.ui import InputText, Modal
from discord.ext import commands, tasks
from hcskr import asyncSelfCheck
import datetime
import asyncio
import json

from setting import hcs_path
file_path = hcs_path

def is_register(DiscordID):
    with open(file_path, "r", encoding="utf_8") as json_file:
        contents = json_file.read()
        json_data = json.loads(contents)
    try:
        a=json_data[f'{DiscordID}']
        return True
    except:
        return False


def add_info(Nickname, DiscordID, Name, Birthday, Area, School, School_lv, Password):
    register = is_register(DiscordID)
    if register:
        return

    data = {}
    with open(file_path, "r", encoding="utf_8") as json_file:
        data = json.load(json_file)

    data[f'{DiscordID}'] = []
    data[f'{DiscordID}'].append({
        "Nickname": f"{Nickname}",
        "DiscordID": f"{DiscordID}",
        "Name": f"{Name}",
        "Birthday": f"{Birthday}",
        "Area": f"{Area}",
        "School": f"{School}",
        "School_lv": f"{School_lv}",
        "Password": f"{Password}",
        "Auto_check": f"X"})

    with open(file_path, 'w',encoding="utf_8") as writefile:
        json.dump(data, writefile, indent="\t", ensure_ascii=False)


def delete_info(DiscordID):
    register = is_register(DiscordID)
    if register:
        with open(file_path, "r", encoding="utf_8") as json_file:
            contents = json_file.read()
            json_data = json.loads(contents)

        json_data.pop(f'{DiscordID}')
        
        with open(file_path, 'w',encoding="utf_8") as writefile:
            json.dump(json_data, writefile, indent="\t", ensure_ascii=False)

        return True
    else:
        return False


def seconds_until(hours, minutes):
    given_time = datetime.time(hours, minutes)
    now = datetime.datetime.now()
    future_exec = datetime.datetime.combine(now, given_time)
    if (future_exec - now).days < 0:  # If we are past the execution, it will take place tomorrow
        future_exec = datetime.datetime.combine(now + datetime.timedelta(days=1), given_time) # days always >= 0
        return (future_exec - now).total_seconds()

class hcs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def my_job_forever(self):
        while True:  # Or change to self.is_running or some variable to control the task
            await asyncio.sleep(seconds_until(7,10))  # Will stay here until your clock says 11:58
            json_object = json.load(open(hcs_path,encoding="utf_8"))
            for k, v in json_object.items():
                if v[0]['Auto_check'] == "O":
                    Nickname = v[0]['Nickname']
                    Name = v[0]['Name']
                    Birthday = v[0]['Birthday']
                    Area = v[0]['Area']
                    School = v[0]['School']
                    School_lv = v[0]['School_lv']
                    Password = v[0]['Password']
                    hcskr_result = asyncSelfCheck(Name, Birthday, Area, School, School_lv, Password)
                    if hcskr_result['code'] == 'SUCCESS':
                        print(f"[자동화] {Nickname} : 자가진단 완료")
                    else:
                        print(f"[자동화] {Nickname} : 자가진단 실패")
            await asyncio.sleep(60)  # Practical solution to ensure that the print isn't spammed as long as it is 11:58


    @slash_command(description="교육부 자가진단을 진행합니다.")
    async def 자가진단(self, ctx, 작업:Option(str,"다음 중 하나를 선택하세요.", choices=["실행", "예약", "등록", "삭제"])):

        errorlist = {"FORMET":"존재하지 않는 지역, 학교급", "NOSCHOOL":"학교 검색 실패", "NOSTUDENT":"학생 검색 실패", "UNKNOWN":"알 수 없는 에러"}
        TrueFalse = is_register(ctx.author.id)
        UserID = str(ctx.author.id)


        if 작업 == "실행":
            if TrueFalse:
                with open(file_path, "r", encoding="utf_8") as json_file:
                    json_data = json.load(json_file)
                #print(json_data[UserID][0])
                Name = json_data[UserID][0]['Name']
                Birthday = json_data[UserID][0]['Birthday']
                Area = json_data[UserID][0]['Area']
                School = json_data[UserID][0]['School']
                School_lv = json_data[UserID][0]['School_lv']
                Password = json_data[UserID][0]['Password']


                hcskr_result = await asyncSelfCheck(Name, Birthday, Area, School, School_lv, Password)
                if hcskr_result['code'] == 'SUCCESS':
                    Success = discord.Embed(title="자가진단이 완료되었습니다.", description=f'완료시각: {hcskr_result["regtime"]}', color=0xffdc16)
                    Success.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/961565520451235840/hcskr.png')
                    await ctx.respond(embed=Success)
                else:
                    error_reason = errorlist[hcskr_result['code']]
                    fail = discord.Embed(title="자가진단이 실패했습니다.", description=f'사유: {error_reason}', color=0xffdc16)
                    fail.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/961565520451235840/hcskr.png')
                    await ctx.respond(embed=fail)
            else:
                No_info = discord.Embed(title="자가진단 정보가 입력되어있지 않습니다.", description=f"`/자가진단 등록`으로 ­자가진단 정보를 입력해주세요.", color=0xffdc16)
                No_info.set_thumbnail(url='https://cdn.discordapp.com/attachments/731471072310067221/871987758510518282/clipart2415195.png')
                await ctx.respond(embed=No_info)


        if 작업 == "삭제":
            Delete = discord.Embed(title=f"{self.bot.user.name} 자가진단", description="­", color=0xffdc16)
            Delete.add_field(name="진단정보 제거시 `/자가진단 진행`을 사용할 수 없습니다.", value="자가진단 정보를 제거하시려면 `1분`내로 ✅를 클릭해주세요.", inline=False)
            Delete.set_thumbnail(url='https://cdn.discordapp.com/attachments/731471072310067221/872301891197997086/093554.png')

            Success_del = discord.Embed(title=f"{ctx.author.name}님의 진단정보 삭제가 완료되었습니다.", description="추후 자가진단을 진행하시려면 다시 `/자가진단 등록`을 입력해주세요", color=0xffdc16)
            Success_del.set_thumbnail(url='https://cdn.discordapp.com/attachments/731471072310067221/872301891197997086/093554.png')

            Failed_del = discord.Embed(title="진단정보 삭제가 취소되었습니다", description="­자가진단 정보를 삭제하시려면 다시 `/자가진단 삭제`를 입력해주세요.", color=0xffdc16)
            Failed_del.set_thumbnail(url='https://cdn.discordapp.com/attachments/731471072310067221/872301891197997086/093554.png')

            if TrueFalse:
                class Button(discord.ui.View):
                    @discord.ui.button(style=discord.ButtonStyle.green, emoji="✅")
                    async def OK(self, button: discord.ui.Button, interaction: discord.Interaction):
                        TrueFalse = delete_info(ctx.author.id)
                        if TrueFalse:
                            await Question.edit_original_message(embed=Success_del, view=None)

                    @discord.ui.button(style=discord.ButtonStyle.red, emoji="⛔")
                    async def Nope(self, button: discord.ui.Button, interaction: discord.Interaction):
                        await Question.edit_original_message(embed=Failed_del, view=None)

                    async def on_timeout(self):
                        await Question.edit_original_message(embed=Failed_del, view=None)

                Question = await ctx.respond(embed=Delete, view=Button(timeout=60))
            else:
                not_reg = discord.Embed(title="등록되지 않은 사용자입니다.", description="자가진단 정보를 입력하시려면 `/자가진단 등록`을 입력해주세요", color=0xffdc16)
                not_reg.set_thumbnail(url='https://cdn.discordapp.com/attachments/731471072310067221/871987758510518282/clipart2415195.png')
                await ctx.respond(embed=not_reg)


        if 작업 == "등록":
            register = discord.Embed(title=f"{self.bot.user.name} 자가진단", description="­자가진단 정보 입력시  `자가진단용 정보가 저장`되어\n`/자가진단 진행`을 사용할 수 있습니다.", color=0xffdc16)
            register.add_field(name="­", value="❗ 자가진단 정보를 확인하기 위해 `1회 자가진단이 진행됩니다.`\n\n자가진단 정보를 입력하시려면 `1분`내로 ✅를 클릭해주세요.", inline=False)
            register.set_thumbnail(url='https://cdn.discordapp.com/attachments/731471072310067221/871987758510518282/clipart2415195.png')

            Success_reg = discord.Embed(title=f"{ctx.author}님의 자가진단 정보 입력이 완료되었습니다.", description="`/자가진단 진행`으로 자가진단을 진행할 수 있습니다.",color=0xffdc16)
            Success_reg.set_thumbnail(url='https://cdn.discordapp.com/attachments/731471072310067221/871987758510518282/clipart2415195.png')

            Already_reg = discord.Embed(title="이미 정보가 입력되어 있습니다.", description="­자가진단 정보를 삭제하시려면 `/자가진단 삭제`를 입력해주세요", color=0xffdc16)
            Already_reg.set_thumbnail(url='https://cdn.discordapp.com/attachments/731471072310067221/871987758510518282/clipart2415195.png')

            Stop_reg = discord.Embed(title="자가진단 등록이 취소되었습니다.", description="­자가진단 정보를 입력하시려면 다시 `/자가진단 등록`을 입력해주세요", color=0xffdc16)
            Stop_reg.set_thumbnail(url='https://cdn.discordapp.com/attachments/731471072310067221/871987758510518282/clipart2415195.png')

            if TrueFalse:
                await ctx.respond(embed=Already_reg)
            else:
                class infoQ(Modal):
                    def __init__(self) -> None:
                        super().__init__("자가진단 정보 입력하기")
                        self.add_item(InputText(label="이름",placeholder="본인의 본명을 입력해주세요.",max_length=30))
                        self.add_item(InputText(label="생년월일",placeholder="6자리 생년월일을 작성해주세요. (ex 051010)",max_length=6))
                        self.add_item(InputText(label="지역",placeholder="학교가 속한 지역을 작성해주세요. (ex 부산)",max_length=30))
                        self.add_item(InputText(label="학교명",placeholder='학교의 이름을 "정확히" 작성해주세요. (ex 부산중학교)',max_length=30))
                        self.add_item(InputText(label="비밀번호",placeholder="자가진단 비밀번호를 작성해주세요.",max_length=4))

                    async def callback(self, interaction:discord.Interaction):
                        if self.children[3].value.find("고등학교") > -1:
                            School_lv = "고등학교"
                        elif self.children[3].value.find("중학교") > -1:
                            School_lv = "중학교"
                        elif self.children[3].value.find("초등학교") > -1:
                            School_lv = "초등학교"
                        elif self.children[3].value.find("특수학교") > -1:
                            School_lv = "특수학교"

                        Name = self.children[0].value
                        Birthday = self.children[1].value
                        Area = self.children[2].value
                        School = self.children[3].value
                        Password = self.children[4].value

                        class Button(discord.ui.View):
                            @discord.ui.button(style=discord.ButtonStyle.green, emoji="✅")
                            async def OK(self, button: discord.ui.Button, interaction: discord.Interaction):
                                hcskr_result = await asyncSelfCheck(Name, Birthday, Area, School, School_lv, Password)
                                try:
                                    if hcskr_result['code'] == 'SUCCESS':
                                        add_info(ctx.author.name, ctx.author.id, Name, Birthday, Area, School, School_lv, Password)
                                        await Question.edit_original_message(embed=Success_reg, view=None)
                                except:
                                    error_reason = errorlist[hcskr_result['code']]
                                    Failed_reg = discord.Embed(title="자가진단 정보 등록에 실패했습니다.", description=f'정보를 모두 "정확히" 입력했는지 확인해주세요\n 입력된 오류: {error_reason}', color=0xffdc16)
                                    Failed_reg.set_thumbnail(url='https://cdn.discordapp.com/attachments/731471072310067221/871987758510518282/clipart2415195.png')
                                    await Question.edit_original_message(embed=Failed_reg)
                                
                            @discord.ui.button(style=discord.ButtonStyle.red, emoji="⛔")
                            async def Nope(self, button: discord.ui.Button, interaction: discord.Interaction):
                                await Question.edit_original_message(embed=Stop_reg, view=None)

                            async def on_timeout(self):
                                await Question.edit_original_message(embed=Stop_reg, view=None)

                        Question = await interaction.response.send_message(embed=register,view=Button(timeout=60))
                await ctx.interaction.response.send_modal(infoQ())

        if 작업 == "예약":
            Auto_on = discord.Embed(title=f"{self.bot.user.name} 자가진단 매크로", description="­이제부터 자가진단이 매일 오전 6시에 진행됩니다.", color=0xffdc16)
            Auto_on.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/961565520451235840/hcskr.png')

            Auto_off = discord.Embed(title=f"{self.bot.user.name} 자가진단 매크로", description="­이제부터 자동 자가진단이 종료됩니다.", color=0xffdc16)
            Auto_off.set_thumbnail(url='https://cdn.discordapp.com/attachments/955355332983521300/961565520451235840/hcskr.png')

            if TrueFalse:
                with open(file_path, "r", encoding="utf_8") as json_file:
                    json_data = json.load(json_file)

                if json_data[UserID][0]['Auto_check'] == "O":
                    json_data[UserID][0]['Auto_check'] = "X"
                    await ctx.respond(embed=Auto_off)
                else:
                    json_data[UserID][0]['Auto_check'] = "O"
                    await ctx.respond(embed=Auto_on)

                with open(file_path, 'w',encoding="utf_8") as writefile:
                    json.dump(json_data, writefile, indent="\t", ensure_ascii=False)
            else:
                not_reg = discord.Embed(title="등록되지 않은 사용자입니다.", description="자가진단 정보를 입력하시려면 `/자가진단 등록`을 입력해주세요", color=0xffdc16)
                not_reg.set_thumbnail(url='https://cdn.discordapp.com/attachments/731471072310067221/871987758510518282/clipart2415195.png')
                await ctx.respond(embed=not_reg)
                return


def setup(bot):
    bot.add_cog(hcs(bot))
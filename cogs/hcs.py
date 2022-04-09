import discord
from discord.commands import slash_command, Option
from discord.ext import commands
from hcskr import asyncSelfCheck


import setting


class hcs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @slash_command(guild_ids = [setting.test_guild], description="교육부 자가진단을 진행합니다.")
    async def 자가진단(self, ctx, 이름:Option(str,"본인의 이름을 작성해주세요."), 생년월일:Option(str,"6자리 생년월일을 작성해주세요. (ex 051010"),
        지역:Option(str,"학교가 속한 지역을 작성해주세요. (ex 부산)"), 학교명:Option(str,"학교의 이름을 작성해주세요. (ex 부산중학교)"),
        학교분류:Option(str,"학교종류를 작성해주세요. (ex 중학교)"), 비밀번호:Option(str,"자가진단 비밀번호를 작성해주세요.")):

        hcs_result = await asyncSelfCheck(이름, 생년월일, 지역, 학교명, 학교분류, 비밀번호)

        if hcs_result['code'] == 'SUCCESS':
            await ctx.respond(embed=discord.Embed(title=f'{ctx.author}님이 요청하신 자가진단이 완료되었습니다.', description='완료시각: '+ hcs_result['regtime'], color=0xf8e71c))
        else:
            errorlist = {"FORMET":"존재하지 않는 지역, 학교급", "NOSCHOOL":"학교 검색 실패", "NOSTUDENT":"학생 검색 실패", "UNKNOWN":"알 수 없는 에러"}
            errorreason = errorlist[hcs_result['code']]
            await ctx.respond(embed=discord.Embed(title=f'{ctx.author}님이 요청하신 자가진단을 진행하지 못했습니다.', description=f'사유: {errorreason}', color=0xf8e71c))
            return


def setup(bot):
    bot.add_cog(hcs(bot))
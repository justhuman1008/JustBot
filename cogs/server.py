import discord
from discord.commands import slash_command
from discord.ext import commands
import asyncio

import setting

class server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids = [setting.test_guild], description="이 서버에 대한 정보를 불러옵니다.")
    async def 서버정보(self, ctx):
        current_guild: discord.Guild = ctx.guild

        safety_settings = {"2FA Setting": current_guild.mfa_level,"verification level": current_guild.verification_level}
        # 보안 레벨
        if safety_settings['verification level'] == discord.VerificationLevel.none:
            safety_settings['verification level'] = "제한 없음"
        elif safety_settings['verification level'] == discord.VerificationLevel.low:
            safety_settings['verification level'] = "이메일 인증 필요"
        elif safety_settings['verification level'] == discord.VerificationLevel.medium:
            safety_settings['verification level'] = "가입후 5분 대기 필요"
        elif safety_settings['verification level'] == discord.VerificationLevel.high or safety_settings['verification level'] == discord.VerificationLevel.table_flip:
            safety_settings['verification level'] = "참여후 10분 대기 필요"
        elif safety_settings['verification level'] == discord.VerificationLevel.extreme or safety_settings['verification level'] == discord.VerificationLevel.double_table_flip:
            safety_settings['verification level'] = "휴대폰 인증 필요"
        
        # Embed
        roles = ctx.guild.roles
        guild_info = discord.Embed(title=f"{current_guild.name}", colour=0xffdc16)
        guild_info.add_field(name="서버 ID", value=f"`{current_guild.id}`", inline=True)
        guild_info.add_field(name="서버 주인", value=f"`{current_guild.owner}`", inline=True)
        guild_info.add_field(name='서버 최고 역할', value=f'{roles[-1].mention}', inline=True)
        guild_info.add_field(name="텍스트 채널 ", value=f"`{len(current_guild.text_channels)}개`", inline=True)
        guild_info.add_field(name="음성 통화방 ", value=f"`{len(current_guild.voice_channels)}개`", inline=True)
        guild_info.add_field(name="카테고리 ", value=f"`{str(len(ctx.guild.categories))}개`", inline=True)
        guild_info.add_field(name="유저", value=f"`{current_guild.member_count}명`", inline=True)
        guild_info.add_field(name='역할수', value="`"+str(len(ctx.guild.roles)) + '개`', inline=True)
        guild_info.add_field(name="이모지 수", value =f'`{len(ctx.guild.emojis)}개`', inline=True)
        guild_info.add_field(name="서버 보안 수준", value=f"`{safety_settings['verification level']}`", inline=True)
        guild_info.add_field(name ='부스트 레벨', value = f"`{current_guild.premium_tier}`", inline =True)
        guild_info.add_field(name="서버 생성 일자", value=f'`{ctx.guild.created_at.strftime("%Y-%m-%d %I")}`', inline=True)
        guild_info.set_thumbnail(url=current_guild.icon)
        await ctx.respond(embed=guild_info)


    @slash_command(guild_ids = [setting.test_guild], description="채널의 메시지를 대량으로 삭제합니다.")
    @commands.has_permissions(manage_messages=True)
    async def 청소(self, ctx, 삭제수량 : int):
        if 삭제수량 <= 0:
            await ctx.respond(embed=discord.Embed(title=f"0보다 큰 수를 입력해주세요.", color=0xf8e71c))
            return
        await ctx.channel.purge(limit=삭제수량)
        await asyncio.sleep(1)
        deletenotice = await ctx.respond(embed=discord.Embed(title=f"메시지 {삭제수량}개를 성공적으로 삭제하였습니다.", color=0xf8e71c))
        await deletenotice.delete_original_message(delay=1)


    @slash_command(guild_ids = [setting.test_guild], description="멘션한 유저를 추방합니다.")
    @commands.has_permissions(ban_members=True)
    async def 추방(self, ctx, 추방할유저:discord.User, 사유=None):
        member = 추방할유저
        reason = 사유
        if member.id == ctx.author.id: 
            await ctx.respond(embed=discord.Embed(title=f"자기 자신은 추방할 수 없습니다.", color=0xf8e71c))
            return
        else:
            if reason == None:
                reason = "추방사유 미작성됨"
            await member.kick(reason=사유)
            kick=discord.Embed(title=f"[추방] {member.name}#{ctx.author.discriminator}", color=0xf8e71c)
            kick.add_field(name=f"대상", value=f"{member.mention}", inline=True)
            kick.add_field(name=f"실행자", value=f"{ctx.author.mention}", inline=True)
            kick.add_field(name=f"사유", value=f"{reason}", inline=False)
            kick.set_thumbnail(url=member.display_avatar)
            await ctx.respond(embed=kick)


    @slash_command(guild_ids = [setting.test_guild], description="멘션한 유저를 차단합니다.")
    @commands.has_permissions(ban_members=True)
    async def 차단(self, ctx, 차단할유저:discord.User, 사유=None):
        member = 차단할유저
        reason = 사유
        if member.id == ctx.author.id: 
            await ctx.respond(embed=discord.Embed(title=f"자기 자신은 추방할 수 없습니다.", color=0xf8e71c))
            return
        else:
            if reason == None:
                reason = "차단사유 미작성됨"
            await member.ban(reason=사유)
            ban=discord.Embed(title=f"[차단] {member.name}#{ctx.author.discriminator}", color=0xf8e71c)
            ban.add_field(name=f"대상", value=f"{member.mention}", inline=True)
            ban.add_field(name=f"실행자", value=f"{ctx.author.mention}", inline=True)
            ban.add_field(name=f"사유", value=f"{reason}", inline=False)
            ban.set_thumbnail(url=member.display_avatar)
            await ctx.respond(embed=ban)


    @slash_command(guild_ids = [setting.test_guild], description="내 디스코드 정보를 불러옵니다.")
    async def 내정보(self, ctx):
        user_info = discord.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator}", colour=0xffdc16)
        user_info.add_field(name="별명", value="`"+ctx.author.display_name+"`", inline=True)
        user_info.add_field(name="유저 ID", value="`"+str(ctx.author.id)+"`", inline=True)
        user_info.add_field(name="역할", value="`"+str(ctx.author.top_role)+"`", inline=True)
        user_info.add_field(name="계정 생성일", value="`"+str(ctx.author.created_at.strftime("%Y %B %d %a"))+"`", inline=True)
        user_info.add_field(name="서버 참가일", value="`"+str(ctx.author.joined_at.strftime("%Y %B %d %a"))+"`", inline=True)
        user_info.set_thumbnail(url=ctx.author.display_avatar)
        await ctx.respond(embed=user_info)


    @slash_command(guild_ids = [setting.test_guild], description="이 서버의 초대링크를 생성합니다.")
    @commands.has_permissions(create_instant_invite=True)
    async def 초대링크(self, ctx, 사용가능횟수:int=10):
        uses = 사용가능횟수
        invitelink = await ctx.channel.create_invite(max_uses=uses, unique=True)
        await ctx.respond(f'> **{ctx.guild}** 서버의 초대링크를 생성하였습니다(`{uses}회 제한`)\n> {invitelink}')


    @slash_command(guild_ids = [setting.test_guild], description="서버에 새로운 역할을 생성합니다.")
    @commands.has_permissions(manage_roles=True)
    async def 역할생성(self, ctx, 역할명):
        role = 역할명
        await ctx.guild.create_role(name=role,colour=discord.Colour(0xf8e71c))
        await ctx.respond(embed=discord.Embed(title=f"역할 `{role}`이(가) 생성되었습니다.", color=0xf8e71c))


    @slash_command(guild_ids = [setting.test_guild], description="서버에 새로운 텍스트 채널을 생성합니다.")
    @commands.has_permissions(manage_channels=True)
    async def 채널생성(self, ctx, 채널명):
        channel = 채널명
        newchannel = await ctx.guild.create_text_channel(channel)
        newchnl = discord.Embed(title=f"새로운 채널을 생성하였습니다.", description=f"<#{newchannel.id}>", colour=0xffdc16)
        await ctx.respond(embed=newchnl)
        return


    @slash_command(guild_ids = [setting.test_guild], description="서버에 새로운 음성 채널을 생성합니다.")
    @commands.has_permissions(manage_channels=True)
    async def 통화방생성(self, ctx, 채널명):
        channel = 채널명
        newchannel = await ctx.guild.create_voice_channel(channel)
        newvchnl = discord.Embed(title=f"새로운 음성 채널을 생성하였습니다.", description=f"<#{newchannel.id}>", colour=0xffdc16)
        await ctx.respond(embed=newvchnl)
        return


    @slash_command(guild_ids = [setting.test_guild], description="서버에 새로운 카테고리를 생성합니다.")
    @commands.has_permissions(manage_channels=True)
    async def 카테고리생성(self, ctx, 카테고리명):
        name = 카테고리명
        await ctx.guild.create_category(name)
        newctg = discord.Embed(title=f"새로운 카테고리를 생성하였습니다.", description=f"카테고리명 `{name}`", colour=0xffdc16)
        await ctx.respond(embed=newctg)
        return


    @slash_command(guild_ids = [setting.test_guild], description="채널에 슬로우모드를 겁니다.")
    @commands.has_permissions(manage_channels=True)
    async def 슬로우모드(self, ctx, 초: int):
        num = 초
        
        if num < 0:
            await ctx.respond(embed=discord.Embed(title="0보다 큰 수를 입력해주세요.", color=0xf8e71c))
            return
        await ctx.channel.edit(slowmode_delay=num)
        if num == 0:
            await ctx.respond(embed=discord.Embed(title=':clock1:'+" 슬로우모드가 해제되었습니다.", color=0xf8e71c))
            return
        await ctx.respond(embed=discord.Embed(title=':clock1:'+f" 이 채널에 `{num}`초 슬로우모드가 적용되었습니다.", color=0xf8e71c))




def setup(bot):
    bot.add_cog(server(bot))
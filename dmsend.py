
# 봉순#4888 : MASS DM BOT SOURCE
# 오픈소스 이용하여 제작되었습니다


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('트라 DM봇')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    #메시지 관리권한이 있을시 사용가능
                    if message.author.guild_permissions.manage_messages:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at)
                        embed.add_field(name="트라 DM봇", value=msg, inline=True)
                        embed.set_footer(text=f"discord.gg/KuJP7R2")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzQ3OTgxMjE0NTQ3MTgxNjAw.X0Wxyg.HDMrS5t0u63yWsAVJ3eo7MWTfjk')

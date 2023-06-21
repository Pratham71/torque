import discord
from discord.ext import commands

class SAY(commands.Cog):
    def __init__(self,client):
       self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
       print('say.py has been loaded')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def say(self,ctx,channel,*,content=None):
        check_channel = discord.utils.get(ctx.guild.channels , name=channel)
        save=content
        await check_channel.send(save)

async def setup(client):
    await client.add_cog(SAY(client))
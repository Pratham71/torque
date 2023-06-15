import discord
from discord.ext import commands

class PING(commands.Cog):
    def __init__(self,client):
       self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
       print('ping.py has been loaded!')

    @commands.command()
    async def ping(self,ctx):
       bot_ping=round(self.client.latency*1000)
       await ctx.reply(f"🏓Pong! {bot_ping}ms.")

async def setup(client):
    await client.add_cog(PING(client))
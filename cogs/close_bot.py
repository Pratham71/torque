import discord
import os
from discord.ext import commands

class CloseBot(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.Cog.listener()
  async def on_ready(self):
    print('close_bot.py has been loaded!')

  @commands.command()
  @commands.is_owner()
  async def close(self,ctx):
    response = "``` Going Offline ```"
    await ctx.reply(response)
    await self.client.close()

async def setup(client):
  await client.add_cog(CloseBot(client))
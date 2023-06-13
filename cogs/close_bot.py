import discord
import os
from discord.ext import commands
ID=397679536818487296
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

  @close.error
  async def close_error(self,ctx,error):
    if ctx.author.id != ID:
      await ctx.reply(f'**ERROR: Forbidden action!**')

async def setup(client):
  await client.add_cog(CloseBot(client))
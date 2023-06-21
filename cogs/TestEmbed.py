import discord
import datetime
from discord.ext import commands

class TestEmbed(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('TestEmbed.py has been loaded!')

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_messages=True)
  async def tmbed(self,ctx):
    embed=discord.Embed(title='**This is a title**',description='This is the description.',color=discord.Color.random())
    embed.add_field(name='**this a field inline is true**',value='the content or value for the field',inline=True)
    embed.add_field(name='**this a field inline is false**',value='the content or value for the field',inline=False)
    embed.set_footer(text='**this is the footer** ar but can be kept as anyhting**')
    embed.set_author(name='**this the author** url= none (can be a redirect url to a page)')
    await ctx.reply(embed=embed)
async def setup(client):
  await client.add_cog(TestEmbed(client))
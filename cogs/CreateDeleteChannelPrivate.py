import discord
from discord.ext import commands

class CDChannelPrivate(commands.Cog):
   def __init__(self,client):
      self.client = client
   
   @commands.Cog.listener()
   async def on_ready(self):
      print('CreateChannelPrivate.py has been loaded!')
      
   
   @commands.command()
   @commands.guild_only()
   @commands.has_permissions(manage_channels=True)
   @commands.bot_has_permissions(manage_channels=True)
   async def createchannelprivate(self,ctx,channel):
      guild = ctx.guild
      overwrites={
         guild.default_role:discord.PermissionOverwrite(view_channel=False)
      }
      await guild.create_text_channel(name=f'{channel}',overwrites=overwrites)
      embed = discord.Embed(title="**Private Channel Created!**",description=f'Channel: **{channel.id}** has been created!',color=discord.Color.green())
      await ctx.send(embed=embed)
   
async def setup(client):
   await client.add_cog(CDChannelPrivate(client))
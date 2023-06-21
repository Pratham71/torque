import discord
from discord.ext import commands

class MemberRoleList(commands.Cog):
   def __init__(self,client):
      self.client = client

   @commands.Cog.listener()
   async def on_ready(self):
      print('MemberRoleList.py is ready!')

   @commands.command()
   async def RoleMember(self,ctx,role:discord.Role):
      log_channel=discord.utils.get(role.guild.channels,name='log-channel')
      embed=discord.Embed(title=f'T**he Members who have:** {role} ',description=f'{role.members}',color=discord.Color.dark_embed())
      await log_channel.send(embed=embed)
      
async def setup(client):
   await client.add_cog(MemberRoleList(client))
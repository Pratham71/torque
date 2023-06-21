import discord 
from discord.ext import commands
c_error='Manage Messages'
K_error='Kick Members'
b_error='Ban/Unban Members'

class kick(commands.Cog):
  def __init__(self,client):
    self.client = client
    
  @commands.Cog.listener()
  async def on_ready(self):
    print('kick.py has been loaded!')

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(moderate_members=True)
  @commands.bot_has_permissions(moderate_members=True)
  async def kick(self,ctx,member:discord.Member,reason=None):
    log_channel=discord.utils.get(member.guild.channels,name='mod-logs')
    embed=discord.Embed(title='**Member Kicked**',color=discord.Color.brand_red())
    if member.id == ctx.author.id:
      await ctx.reply("**bruh do you hate yourself that much 💀 **")
    else:
      embed.add_field(name='**Name**:',value=f'{member.mention}',inline=True)
      embed.add_field(name='**ID**:',value=f'{member.id}',inline=True)
      embed.add_field(name='**Reason**:',value=reason,inline=False)
      embed.set_thumbnail(url=member.avatar)
      await log_channel.send(embed=embed)
      await ctx.reply(f'check: <#{log_channel.id}>')
      await ctx.guild.kick(member)

  @kick.error
  async def kerror(self,ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
      await ctx.reply(f"Error: Missing Required Arguments!, You must pass a userID or '@' mention to run kick command")
    elif isinstance(error,commands.MissingPermissions):
      await ctx.reply(f"Error: Missing Required Permissions, You must have the required permission(s) assigned to your role(s) \n{K_error}")
    elif isinstance(error,commands.BotMissingPermissions):
      await ctx.reply(f'Error: Bot Missing Required Permissions, The bot must have the required permission(s) assigend to its role(s) \n{K_error}')
async def setup(client):
    await client.add_cog(kick(client))    
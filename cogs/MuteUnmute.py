import discord,datetime
from discord.ext import commands

t_error='moderate members'

class TimeOut(commands.Cog):
  def __init__(self,client):
    self.client = client
    
  @commands.Cog.listener()
  async def on_ready(self):
    print('timeout.py is ready!')
    
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(moderate_members=True)
  @commands.bot_has_permissions(moderate_members=True)
  async def mute(self,ctx,member:discord.Member,minutes: int=0,reason=None):
    log_channel=discord.utils.get(member.guild.channels,name='mod-logs')
    if ctx.author.id == member.id :
      await ctx.reply('**You cannot mute yourself!**')
    duration =  datetime.timedelta(minutes=minutes)
    timeout_embed = discord.Embed(title='**User Muted!**',color=discord.Color.dark_theme())
    timeout_embed.add_field(name='**Name:**',value=f'{member.mention}',inline=True)
    timeout_embed.add_field(name='**User ID:**',value=f'{member.id}',inline=True)
    timeout_embed.add_field(name='**Duration:**',value=f'**{duration}**',inline=True)
    timeout_embed.add_field(name='**Reason:**',value=f'{reason}',inline=True)
    timeout_embed.set_footer(text=f'**Muted by**:{ctx.author}',icon_url=ctx.author.avatar)
        
    await member.timeout(duration)
    await ctx.reply(embed=timeout_embed)
    await log_channel.send(embed=timeout_embed)
      
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(moderate_members=True)
  @commands.bot_has_permissions(moderate_members=True)
  async def unmute(self,ctx,member:discord.Member):
    await member.edit(timed_out_until=None)
    await ctx.send(f'{member.mention} **Has been unmuted!**')

  
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(moderate_members=True)
  @commands.bot_has_permissions(moderate_members=True)
  async def ismuted(self,ctx,member:discord.Member=None):
    if member is None:
      member=ctx.author
    elif member is not None:
      member=member
        
    if member.is_timed_out() ==  True:
      await ctx.reply(f'{member.mention} **is muted**:__{member.is_timed_out()}__')
    else:
      await ctx.reply(f'{member.mention} **is muted**: __{member.is_timed_out()}__')

async def setup(client):
    await client.add_cog(TimeOut(client))
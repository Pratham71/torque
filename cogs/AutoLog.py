import discord,json,time
from discord.ext import commands
from discord.utils import find
whitelist=[1102927006703829014,882471259231887390,746023730488148091,1102164592974639155]
class AutoLog(commands.Cog):
  def __init__(self,client):
    self.client =  client

  @commands.Cog.listener()
  async def on_ready(self):
    print("AutoLog.py has been loaded!")

  @commands.Cog.listener()
  async def on_guild_join(self,guild):

    with open('prefixes.json','r') as f:
      prefixes = json.load(f)
    
    prefixes[str(guild.id)] = 't!'

    with open('prefixes.json','w') as f:
      json.dump(prefixes,f,indent=4)

    whitelist=[1102927006703829014,882471259231887390,746023730488148091,1102164592974639155,1102927006703829014,746023730488148091,1118237629561962618]
    server_id=guild.id
    if server_id in whitelist:
      global channel2
      log_channel_check=discord.utils.get(guild.channels,name='log-channel')
      moderation_command_channel_check=discord.utils.get(guild.channels,name='mod-logs')

      overwrites= {
        guild.default_role: discord.PermissionOverwrite(view_channel = False)
      }

    
      if log_channel_check is None or moderation_command_channel_check is None :
        channel = await guild.create_text_channel('log-channel',overwrites=overwrites)
        channel1 = await guild.create_text_channel('mod-logs',overwrites=overwrites)
        channel2 =  await guild.create_text_channel('spam-logs',overwrites=overwrites)
        print(channel2)
        await channel.send('```THIS CHANNEL HAS BEEN SET FOR AUTO LOGGING!```\n@here')
        await channel1.send('```THIS CHANNEL HAS BEEN SET FOR MOD LOGS ANY COMMAND USED IN THIS SERVER WILL BE LOGGED HERE!```\n@here')
        await channel2.send('```THIS CHANNEL HAS BEEN SET FOR SPAM LOGS!```\n@here')

        print('CHANNEL CREATED!')
      
    else:
      channel = guild.system_channel 
      if channel.permissions_for(guild.me).send_messages: 
        await channel.send(f"I'm not allowed to join **{guild.name}** please ask the owner to give me access to this server!")
        await guild.leave()
        
      with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    
      prefixes.pop(str(guild.id))

      with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)

  @commands.Cog.listener()
  async def on_guild_remove(self,guild):
    with open('prefixes.json','r') as f:
      prefixes = json.load(f)
    
    prefixes.pop(str(guild.id))

    with open('prefixes.json','w') as f:
      json.dump(prefixes,f,indent=4)



  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.client.user:
      return
    else:
      return 'yes'


  
  @commands.Cog.listener()
  async def on_message_delete(self,message):
    log_channel=discord.utils.get(message.guild.channels,name='spam-logs')
    embed=discord.Embed(title=f'**Message deletde in channel:**{message.channel.mention}',description=f'```{message.content}```\n**Deleted by:**{message.author.mention}',color=discord.Color.magenta())
    await log_channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_member_join(self,member):
    log_channel=discord.utils.get(member.guild.channels,name='spam-logs')

    embed=discord.Embed(title='**Arrival Logged**',color=discord.Color.brand_green())
    embed.add_field(name='**Member:**',value=member.mention,inline=True)
    embed.add_field(name='**Member ID:**',value=member.id,inline=True)
    embed.add_field(name='**Creation Date:**',value=member.created_at.__format__('%A,%d. %B %Y @ %H:%M:%S'),inline=False)
    embed.set_image(url=member.avatar)
    await log_channel.send(embed=embed)
  
  @commands.Cog.listener()
  async def on_member_remove(self,member):
    log_channel=discord.utils.get(member.guild.channels,name='spam-logs')
    embed=discord.Embed(title='**Departure Logged**',color=discord.Color.from_rgb(r=171,g=176,b=1))
    embed.add_field(name='**Member:**',value=member.mention,inline=True)
    embed.add_field(name='**Member ID:**',value=member.id,inline=True)
    embed.add_field(name='**Creation Date:**',value=member.created_at.__format__('%A,%d. %B %Y'),inline=False)
    embed.set_image(url=member.avatar)
    await log_channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_guild_role_create(self,role):
    log_channel=discord.utils.get(role.guild.channels,name='spam-logs')

    embed=discord.Embed(title='**Role Created**',color=discord.Color.dark_teal())
    embed.add_field(name='**Role Name**:',value=f'{role.mention}',inline=True)
    embed.add_field(name='**Role ID**:',value=role.id,inline=True)
    embed.add_field(name='**Color:**',value=role.color,inline=True)
    embed.add_field(name='**Mentionable:**',value=role.mentionable,inline=False)
    embed.add_field(name='**Creation Date:**',value=role.created_at.__format__('**%A,%d. %B %Y**'),inline=True)
    await log_channel.send(embed=embed)
  
  @commands.Cog.listener()
  async def on_guild_role_delete(self,role):
    log_channel=discord.utils.get(role.guild.channels,name='spam-logs')

    embed=discord.Embed(title='**Role Deleted**',color=discord.Color.greyple())
    embed.add_field(name='**Role Name**:',value=f'{role.name}',inline=True)
    embed.add_field(name='**Role ID**:',value=role.id,inline=True)
    await log_channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_guild_channel_create(self,channel):
    log_channel=discord.utils.get(channel.guild.channels,name='spam-logs')

    embed=discord.Embed(title='**Channel Created**',color=discord.Color.teal())
    embed.add_field(name='**Channel Name**:',value=f'{channel.mention}',inline=True)
    embed.add_field(name='**Channel ID**:',value=f'{channel.id}',inline=True)
    embed.add_field(name='**Channe Category**:',value=f'{channel.category}',inline=True)
    await log_channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_guild_channel_delete(self,channel):
    log_channel=discord.utils.get(channel.guild.channels,name='spam-logs')

    embed=discord.Embed(title='**Channel Deleted**',color=discord.Color.purple())
    embed.add_field(name='**Channel Name**:',value=f'{channel.name}',inline=True)
    embed.add_field(name='**Channel ID**:',value=f'{channel.id}',inline=True)
    embed.add_field(name='**Channe Category**:',value=f'{channel.category}',inline=True)
    await log_channel.send(embed=embed)

async def setup(client):
  await client.add_cog(AutoLog(client))
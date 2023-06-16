import discord,json 
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
      log_channel_check=discord.utils.get(guild.channels,name='log-channel')
      moderation_command_channel_check=discord.utils.get(guild.channels,name='mod-logs')

      overwrites= {
        guild.default_role: discord.PermissionOverwrite(view_channel = False)
      }

    
      if log_channel_check is None or moderation_command_channel_check is None :
        channel = await guild.create_text_channel('log-channel',overwrites=overwrites)
        channel1 = await guild.create_text_channel('mod-logs',overwrites=overwrites)
        channel2 =  await guild.create_text_channel('spam-logs',overwrites=overwrites)

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
      log_channel = discord.utils.get(message.guild.channels, name='spam-logs')

        
      event_embed = discord.Embed(title='Message Logged',description='Message\'s content and origin',color=discord.Color.dark_blue())
      event_embed.add_field(name='Message Author:',value=message.author.mention,inline=False)
      event_embed.add_field(name='Channel Origin:',value=message.channel.mention,inline=False)
      event_embed.add_field(name='Message Content:',value=message.content,inline=False)

      await log_channel.send(embed=event_embed)
  

      
async def setup(client):
  await client.add_cog(AutoLog(client))

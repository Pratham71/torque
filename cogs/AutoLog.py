import discord 
from discord.ext import commands
from discord.utils import find

class AutoLog(commands.Cog):
  def __init__(self,client):
    self.client =  client

  @commands.Cog.listener()
  async def on_ready(self):
    print("AutoLog.py has been loaded!")

  @commands.Cog.listener()
  async def on_guild_join(self,guild):
    whitelist=[1102927006703829014,882471259231887390,746023730488148091,1102164592974639155]
    server_id=guild.id
    for whitelist_id in whitelist:
      if server_id == whitelist_id:
        log_channel_check=discord.utils.get(guild.channels,name='log-channel')
        moderation_command_channel_check=discord.utils.get(guild.channels,name='mod-logs')

        overwrites= {
          guild.default_role: discord.PermissionOverwrite(view_channel = False),
        }

    
        if log_channel_check is None or moderation_command_channel_check is None :
          channel = await guild.create_text_channel('log-channel',overwrites=overwrites)
          channel1 = await guild.create_text_channel('mod-logs',overwrites=overwrites)
          channel2 =  await guild.create_text_channel('spam-logs',overwrites=overwrites)

          await channel.send('```THIS CHANNEL HAS BEEN SET FOR AUTO LOGGING!```\n@here')
          await channel1.send('```THIS CHANNEL HAS BEEN SET FOR MOD LOGS ANY COMMAND USED IN THIS SERVER WILL BE LOGGED HERE!```\n@here')
          await channel2.send('```THIS CHANNEL HAS BEEN SET FOR SPAM LOGS!```\n@here')

          print('CHANNEL CREATED!')
          break

      else:
        for guild in self.client.guilds:
          channel = guild.system_channel 
          if channel.permissions_for(guild.me).send_messages: 
              await channel.send(f"I'm not allowed to join **{guild.name}** please ask the owner to give me access to this server!")
              await guild.leave()

        
async def setup(client):
  await client.add_cog(AutoLog(client))


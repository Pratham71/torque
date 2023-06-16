import discord,time,platform,colorama,asyncio,os,json
"__________________"
from colorama import Back,Fore,Style
from discord.ext import commands,tasks
from itertools import cycle

def get_prefix(client,message):
  with open('prefixes.json','r') as f:
    prefixes = json.load(f)
  
  return prefixes[str(message.guild.id)]

TOKEN=''
client=commands.Bot(command_prefix=get_prefix,intents=discord.Intents.all())

bot_status = cycle(["in development"])

@client.event
async def on_ready():
  print(f'{client.user} is online!')
  change_status.start()

@tasks.loop(seconds=1)
async def change_status():
  await client.change_presence(activity=discord.Game(next(bot_status)))

async def load_cogs():
  for filename in os.listdir('C:\\Users\\Pratham\\Desktop\\Torque\\cogs'):
    if filename.endswith('.py'):
      await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
  async with client:
    await load_cogs()
    await client.start(TOKEN)

asyncio.run(main())

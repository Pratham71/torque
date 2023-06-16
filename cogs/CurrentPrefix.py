import discord,json
from discord.ext import commands

class CurrentPrefix(commands.Cog):
    def __init__(self,client):
       self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
       print('CurrentPrefix.py is ready!')

    @commands.command()
    async def currentprefix(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes = json.load(f)
  
        z=prefixes[str(ctx.guild.id)]
        await ctx.reply(f"The current prefix for **{ctx.guild.name}** is: __{z}__")


async def setup(client):
    await client.add_cog(CurrentPrefix(client))
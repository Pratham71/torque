import discord,json
from discord.ext import commands

class ChangePrefix(commands.Cog):
    def __init__(self,client):
      self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('ChangePrefix.py is ready!')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @commands.bot_has_permissions(administrator=True)
    async def changeprefix(self,ctx,prefix):
      with open('prefixes.json','r') as f:
        prefixies = json.load(f)
        
      prefixies[str(ctx.guild.id)] = str(prefix)

      with open('prefixes.json','w') as f:
        json.dump(prefixies,f,indent=4)
         
      await ctx.send(f'Prefix has been changed to {prefix} by {ctx.author.mention}')
      

async def setup(client):
    await client.add_cog(ChangePrefix(client))
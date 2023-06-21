import discord,json
from discord.ext import commands

class GuildLeave(commands.Cog):
    def __init__(self,client):
       self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
       print('Guildleave.py has been loaded!')

    @commands.command()
    @commands.is_owner()
    async def leave(self,ctx,*,guild_name):
        guild =  discord.utils.get(self.client.guilds,name=guild_name)
        
        if guild is None:
            await ctx.reply('No guild with that name!')
            return
        else:
            await ctx.reply(f'**I have left {guild_name}!**')
            await guild.leave()
            with open('prefixes.json','r') as f:
                prefixes = json.load(f)
    
            prefixes.pop(str(guild.id))

            with open('prefixes.json','w') as f:
                json.dump(prefixes,f,indent=4)

    @leave.error
    async def leave_error(self,ctx,error):
        if ctx.author.id != 397679536818487296:
            await ctx.reply(f'**Error: Your are forbiddened from using this command!! __only the owner of this bot can use it__**')

async def setup(client):
    await client.add_cog(GuildLeave(client))
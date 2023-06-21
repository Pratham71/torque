import discord,datetime,time
from discord.ext import commands

class Uptime(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        global StartTime
        StartTime = time.time()
        print('Uptime.py has been loaded!')
    
    @commands.command()
    @commands.guild_only()
    async def time(self,ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-StartTime))))
        time_embed = discord.Embed(title=f'**{self.client.user}\'s Uptime**',color=discord.Color.light_grey())
        time_embed.add_field(name='__Uptime:__',value=uptime)
        time_embed.set_footer(text=f'Requested by {ctx.author}',icon_url=ctx.author.avatar)
        await ctx.send(embed=time_embed) 
    
async def setup(client):
    await client.add_cog(Uptime(client))
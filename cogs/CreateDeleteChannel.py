import discord
from discord.ext import commands

class CDChannel(commands.Cog):
    def __init__(self,client):
       self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
       print('CreateDeleteChannel.py has been loaded!')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def deletechannel(self,ctx,channel:discord.TextChannel):
        embed =  discord.Embed(title='**Channel Deleted!**',description=f'Channel: <#{channel.id}> has been deleted!',color=discord.Color.red())
        await ctx.send(embed=embed)
        await channel.delete()
    
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def createchannel(self,ctx,channel):
        guild = ctx.guild
        await guild.create_text_channel(name=f'{channel}')
        embed = discord.Embed(title="**Channel Created!**",description=f'Channel: **{channel}** has been created!',color=discord.Color.green())
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(CDChannel(client))


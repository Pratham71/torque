import discord
from discord.ext import commands

class Userinfo(commands.Cog):
    def __init__(self,client):
       self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
       print('Userinfo.py has been loaded!')
    
    @commands.command()
    @commands.guild_only()
    async def UserInfo(self,ctx,member: discord.Member=None):
        if member is None:
            member = ctx.author
        elif member is not None:
            member=member
        
        info_embed=discord.Embed(title=f'{member.name}\'s User Info',description=f'All of information about {member.name}',color=discord.Color.random())
        info_embed.set_thumbnail(url=member.avatar)
        info_embed.add_field(name='Name:',value=member.name,inline=False)
        info_embed.add_field(name='Nick Name:',value=member.display_name,inline=False)
        info_embed.add_field(name='Disciminator:',value=member.discriminator,inline=False)
        info_embed.add_field(name='ID:',value=member.id,inline=False)
        info_embed.add_field(name='Top role:',value=member.top_role,inline=False)
        info_embed.add_field(name='Bot user:',value=member.bot,inline=False)
        info_embed.add_field(name='Timed Out?:',value=member.is_timed_out(),inline=False)
        info_embed.add_field(name='Joined this server at:',value=member.joined_at.date(),inline=False)
        info_embed.add_field(name='Creation Date:',value=member.created_at.__format__('%A,%d. %B %Y @ %H:%M:%S'),inline=False)

        await ctx.send(embed=info_embed)
    
    
async def setup(client):
    await client.add_cog(Userinfo(client))
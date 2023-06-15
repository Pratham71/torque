import discord
from discord.ext import commands
b_error='Ban/Unban Members'

class BanUnban(commands.Cog):
    def __init__(self,client):
       self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
       print('BanUnban.py is ready!')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self,ctx,member:discord.Member,*,modreason=None):
        if ctx.author.id == member.id:
            await ctx.reply(f'**You cannot ban your self!**')
        else:
            embed = discord.Embed(title='**BANNED!**',description=f'{member.mention} has been banned from the server by {ctx.author.mention}\n**Member ID**: {member.id}\n**Reason**:{modreason}',color=discord.Color.blurple())
            await ctx.guild.ban(member)
            await ctx.send(embed=embed)
    
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self,ctx,userId):
        user = discord.Object(id=userId)
        if ctx.author.id == userId:
            await ctx.reply(f'**Ok sure Unbanning you!**')
        else:
            conf_embed = discord.Embed(title='**UN-BANNED!**',description=f'<@{userId}> has been Un banned from the server by {ctx.author.mention}',color=discord.Color.blurple())
            await ctx.guild.unban(user)
            await ctx.send(embed=conf_embed)

    @ban.error
    async def ban_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.reply(f"Error: Missing Required Arguments!, You must pass a userID or '@' mention to run ban command")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.reply(f"Error: Missing Required Permissions, You must have the required permission(s) assigned to your role(s) \n**{b_error}**")
        elif isinstance(error,commands.BotMissingPermissions):
            await ctx.reply(f'Error: Bot Missing Required Permissions, The bot must have the required permission(s) assigend to its role(s) \n**{b_error}**')

    @unban.error
    async def unban_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.reply(f"Error: Missing Required Arguments!, You must pass a userID to run unban command")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.reply(f"Error: Missing Required Permissions, You must have the required permission(s) assigned to your role(s) \n**{b_error}**")
        elif isinstance(error,commands.BotMissingPermissions):
            await ctx.reply(f'Error: Bot Missing Required Permissions, The bot must have the required permission(s) assigend to its role(s) \n**{b_error}**')
    
    
async def setup(client):
    await client.add_cog(BanUnban(client))
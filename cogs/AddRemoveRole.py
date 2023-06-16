import discord
from discord.ext import commands

class AddRemoveRole(commands.Cog):
    def __init__(self,client):
       self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
       print('AddRemoveRole.py has been loaded!')

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def addrole(self,ctx,user: discord.Member,*,role: discord.Role):
        if role in user.roles:
            await ctx.send(f'{user.mention} already has the role: {role.mention}')
        else:
            await user.add_roles(role)
            embed=discord.Embed(title='**Role Added!**',description=f"Added the role: {role.mention} to {user.mention}",color=discord.Color.dark_grey())
            await ctx.send(embed=embed)
    
    @addrole.error
    async def role_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command!")
    
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def removerole(self,ctx,user: discord.Member,*,role: discord.Role):
        if role in user.roles:
            await user.remove_roles(role)
            await ctx.send(embed=embed)
            embed=discord.Embed(title='**Role Removed!**',description=f"Removed the role: {role.mention} from {user.mention}",color=discord.Color.dark_grey())
        else:
            await ctx.send(f'{user.mention} does not have the role: {role.mention}')
    
    @removerole.error
    async def removerole_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command!")

async def setup(client):
    await client.add_cog(AddRemoveRole(client))
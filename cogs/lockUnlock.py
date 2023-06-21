import discord
from discord.ext import commands

class lockUnlock(commands.Cog):
   def __init__(self,client):
      self.client = client

   @commands.Cog.listener()
   async def on_ready(self):
      print('lockUnlock.py is ready!')

   @commands.command()
   @commands.has_permissions(administrator=True)
   @commands.guild_only()
   async def lock(self,ctx,role:discord.Role):
      guild=ctx.guild
      role_id=role.id
      cp= role.permissions
      cp.update(#current permission 
        send_messages = False,
        use_application_commands=False,
        send_messages_in_threads=False,
        create_public_threads=False,
        create_private_threads=False,
        change_nickname=False,
        connect=False,
        speak=False,
        video=False,
        use_voice_activity=False
      )
      perms="""send_messages = False,
        use_application_commands=False,
        send_messages_in_threads=False,
        create_public_threads=False,
        create_private_threads=False,
        change_nickname=False,
        connect=False,
        speak=False,
        video=False,
        use_voice_activity=False"""
      await role.edit(permissions=cp)
      embed=discord.Embed(title='**🚨🔒Discord Server in lock Down🔒🚨**',description=f'**🚨🔒Lock Down Actived🔒🚨**\n**Used by {ctx.author.mention}',color=discord.Color.red())
      embed.add_field(name='**Role(s) in lock down:**',value=f'{role.mention}',inline=False)
      embed.add_field(name='**Permission Overwritten:**',value=f'{perms}',inline=False)
      await ctx.reply(embed=embed)
   
   @commands.command()
   @commands.guild_only()
   @commands.has_permissions(administrator=True)
   async def unlock(self,ctx,role:discord.Role):
      guild=ctx.guild
      role_id=role.id
      cp= role.permissions
      cp.update(#current permission 
        send_messages = True,
        use_application_commands=True,
        send_messages_in_threads=True,
        create_public_threads=True,
        create_private_threads=True,
        change_nickname=True,
        connect=True,
        speak=True,
        video=True,
        use_voice_activity=True
      )
      perms="""send_messages = True,
        use_application_commands=True,
        send_messages_in_threads=True,
        create_public_threads=True,
        create_private_threads=True,
        change_nickname=True,
        connect=True,
        speak=True,
        video=True,
        use_voice_activity=True"""
      await role.edit(permissions=cp)
      embed=discord.Embed(title='**🚨🔓Discord Server out of lock Down🔓🚨**',description=f'**🚨🔓Lock Down Deactived🔓🚨**\n**Used by {ctx.author.mention}',color=discord.Color.green())
      embed.add_field(name='**Role(s) out of  lock down:**',value=f'{role.mention}',inline=False)
      embed.add_field(name='**Permission Overwritten:**',value=f'{perms}',inline=False)
      await ctx.reply(embed=embed)
   
async def setup(client):
    await client.add_cog(lockUnlock(client))
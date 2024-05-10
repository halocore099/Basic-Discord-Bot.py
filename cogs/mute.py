import discord
from discord.ext import commands

class mute(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(manage_roles=True)
  async def mute(self, ctx, member: discord.Member):
      muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
      if not muted_role:
          muted_role = await ctx.guild.create_role(name="Muted")
          for channel in ctx.guild.channels:
              await channel.set_permissions(muted_role, send_messages=False)
      await member.add_roles(muted_role)
      await ctx.send(f"{member.mention} has been muted.")
  @commands.command()
  @commands.has_permissions(manage_roles=True)
  async def unmute(self, ctx, member: discord.Member):
      muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
      if muted_role in member.roles:
          await member.remove_roles(muted_role)
          await ctx.send(f"{member.mention} has been unmuted.")
      else:
          await ctx.send(f"{member.mention} is not muted.")

async def setup(bot):
  await bot.add_cog(mute(bot))

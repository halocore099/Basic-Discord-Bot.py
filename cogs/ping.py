import discord
from discord.ext import commands

class ping(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def ping(self, ctx):
      latency = round(self.bot.latency * 1000)  # Convert to milliseconds
      await ctx.send(f'Pong! Latency: {latency}ms')


async def setup(bot):
  await bot.add_cog(ping(bot))

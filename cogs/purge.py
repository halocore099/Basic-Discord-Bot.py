import discord
from discord.ext import commands
import asyncio

class purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def purge(self, ctx, amt):
        await ctx.channel.purge(limit = int(amt) + 1)
        msg = await ctx.send(f"Purged {amt} messages.")
        await asyncio.sleep(3)
        await msg.delete

async def setup(bot):
    await bot.add_cog(purge(bot))

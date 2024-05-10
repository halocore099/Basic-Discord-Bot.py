from discord.ext import commands
import requests
import discord

class Dog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dog(self, ctx):
        r = requests.get("https://dog.ceo/api/breeds/image/random/")
        res = r.json()

        embed = discord.Embed()
        embed.set_image(url=res['message'])

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Dog(bot))

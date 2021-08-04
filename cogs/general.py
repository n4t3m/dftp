import discord
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Events

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is Online!")

    #Commands
    
    @commands.command()
    async def ping(self, ctx):
        embed=discord.Embed()
        embed.add_field(name="Ping", value='Pong! {0}'.format(round(self.bot.latency, 1)))
        await ctx.send(embed=embed)



    
def setup(bot):
    bot.add_cog(General(bot))

import discord
from discord.ext import commands
import config
import os
import asyncio

class DFTP(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.GUILD_UID = config.GUILD_UID
        self.OWNER_UID = config.OWNER_UID

    #Events

    @commands.Cog.listener()
    async def on_ready(self):
        print(os.path.basename(__file__)[:-3].upper() + " loaded succesfully!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != self.OWNER_UID:
            return
        if message.channel.name == "uploads" and message.guild.id == self.GUILD_UID:
            return
        return

    @commands.command()
    async def init(self, ctx):
        m = await ctx.send("Make sure this command is run in a brand new server....")
        await asyncio.sleep(3)
        await m.delete()

        guild = ctx.guild

        for c in ctx.guild.channels:
            await c.delete()

        await guild.create_text_channel('downloads')
        await guild.create_text_channel('uploads')
        
        return

    
def setup(bot):
    bot.add_cog(DFTP(bot))

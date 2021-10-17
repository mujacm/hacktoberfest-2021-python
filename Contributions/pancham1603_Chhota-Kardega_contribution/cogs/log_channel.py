from discord.ext import commands
import discord
import json


class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['log-channel'])
    async def _log_channel(self, ctx, channel=None):
        if not channel:
            embed = discord.Embed(title='Please mention the ID of the discord channel', color = discord.Color.red())
            await ctx.send(embed=embed)
        else:
            if int(ctx.author.id) in [543869441835008000, 690519146701783042]:
                channel = json.dumps({"channel":int(channel)}, indent=4)
                with open("log_channel.json", 'w') as file:
                    file.write(channel)
                await ctx.send('Changed')
            else:
                embed = discord.Embed(title='You are not permitted to use this command', color = discord.Color.red())
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Startup(bot))
import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def osweexam(ctx):
    channel = ctx.channel
    msg = "https://help.offensive-security.com/hc/en-us/articles/360046869951-OSWE-Exam-Guide"
    await channel.send(msg)

def setup(bot):
    bot.add_command(osweexam)

def teardown(bot):
    bot.remove_command(osweexam)
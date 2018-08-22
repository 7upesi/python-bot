import discord
import random
import config
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='A bot that does whatever I tell it to')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def thetruth(ctx):
    await ctx.send("traps are gay!")

@bot.command()
async def roll(ctx, dice: str):
    diceNum = 0
    dieNum = 0
    endRoll = 0
    parameter1 = dice.split("d", 1)
    diceNum = int(parameter1.pop(0))
    parameter2 = parameter1.pop(0)
    if parameter2.isdigit():
        dieNum = int(parameter2)
        for _ in range(diceNum):
            endRoll += random.randint(1, dieNum + 1)
    else:
        parameter3 = parameter2.split("-", 1)
        dieNum = int(parameter3.pop(0))
        if(parameter3.len == 1):
            addNum = int(parameter3.pop(0))
            for _ in range(diceNum):
                endRoll += random.randint(1, dieNum + 1) + addNum
        else:
            subNum = int(parameter3.pop(0))
            for _ in range(diceNum):
                endRoll += random.randint(1, dieNum + 1) - subNum
    await ctx.send(endRoll)

bot.run(config.token)
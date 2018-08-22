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
async def rolladv(ctx):
    firstRoll = random.randint(1, 20)
    secondRoll = random.randint(1, 20)
    if(firstRoll > secondRoll):
       await ctx.send(str(firstRoll) + " (lower roll was " + str(secondRoll) + ")")
    else:
       await ctx.send(str(secondRoll) + " (lower roll was " + str(firstRoll) + ")")

@bot.command()
async def rolldav(ctx):
    firstRoll = random.randint(1, 20)
    secondRoll = random.randint(1, 20)
    if(firstRoll > secondRoll):
      await  ctx.send(str(secondRoll) + " (higher roll was " + str(firstRoll) + ")")
    else:
      await  ctx.send(str(firstRoll) + " (higher roll was " + str(secondRoll) + ")")

@bot.command()
async def roll(ctx, dice: str):
    diceNum = 0
    dieNum = 0
    endRoll = 0
    parameter1 = dice.split("d", 1)
    diceNum = int(parameter1.pop(0))
    parameter2 = parameter1.pop(0)
    rolls = []
    if parameter2.isdigit():
        dieNum = int(parameter2)
        for _ in range(diceNum):
            currentRoll = random.randint(1, dieNum)
            rolls.append(currentRoll)
            endRoll += currentRoll
    else:
        parameter3 = parameter2.split("-", 1)
        if(len(parameter3) == 1):
            parameter3 = parameter2.split("+", 1)
            dieNum = int(parameter3.pop(0))
            addNum = int(parameter3.pop(0))
            for _ in range(diceNum):
                currentRoll = random.randint(1, dieNum)
                rolls.append(currentRoll)
                endRoll += currentRoll
            endRoll += addNum
        else:
            dieNum = int(parameter3.pop(0))
            subNum = int(parameter3.pop(0))
            for _ in range(diceNum):
                currentRoll = random.randint(1, dieNum)
                rolls.append(currentRoll)
                endRoll += currentRoll
            endRoll -= subNum
    await ctx.send(str(rolls) + " = " + str(endRoll))

bot.run(config.token)
import discord  # Importing libs
import nekos
from discord.ext import commands
from random import *

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$') #Prefix for bot

@bot.event #Allows user to see in Python console that bot has been initialized
async def on_ready():
    activity = discord.Game(name="$commands")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print('We have logged in as {0.user}'.format(bot))

@bot.event #This whole event should allow @bot.command's to go through after @bot.event's.
async def on_message(message):
    await bot.process_commands(message)

@bot.command()
async def add(ctx, left: int, right: int): #User inputs 2 numbers
    await ctx.send(left + right) #Bot adds them together and sends answer

@bot.command()
async def subtract(ctx, left: int, right: int): #User inputs 2 numbers
    await ctx.send(left - right) #Bot subtracts them and sends answer

@bot.command()
async def divide(ctx, left: int, right: int): #User inputs 2 numbers
    await ctx.send(left / right) #Bot divides them and sends answer

@bot.command()
async def multiply(ctx, left: int, right: int): #User inputs 2 numbers
    await ctx.send(left * right) #Bot multiplies them and sends answer

@bot.command()
async def cool(ctx):
    randnum = randint(1, 2)
    if randnum == 1:
        await ctx.send("You are cool!")
    else:
        await ctx.send("You are not cool!")

@bot.command()
async def coinflip(ctx):
    randnum = randint(1, 2)
    if randnum == 1:
        await ctx.send("Heads!")
    else:
        await ctx.send("Tails!")

@bot.command()
async def cat(ctx):
    catimg = nekos.cat()
    await ctx.send(catimg)

@bot.command()
async def fact(ctx):
    fact = nekos.fact()
    await ctx.send(fact)

@bot.command()
async def dog(ctx):
    dogimg = nekos.img("woof")
    await ctx.send(dogimg)

@bot.command()
async def goose(ctx):
    gooseimg = nekos.img("goose")
    await ctx.send(gooseimg)

@bot.command()
async def waifu(ctx):
    waifuimg = nekos.img("waifu")
    await ctx.send(waifuimg)

@bot.command()
async def lizard(ctx):
    lizardimg = nekos.img("lizard")
    await ctx.send(lizardimg)

@bot.command()
async def owoify(ctx, wantowoed):
    userowo = nekos.owoify(wantowoed)
    await ctx.send(userowo)

@bot.command()
async def showerthought(ctx):
    shwrthought = nekos.why()
    await ctx.send(shwrthought)

@bot.command()
async def eightball(ctx, eightballquestion):
    randballnum = randint(1, 20)
    if randballnum == 1:
        await ctx.send("It is certain.")
    elif randballnum == 2:
        await ctx.send("It is decidedly so.")
    elif randballnum == 3:
        await ctx.send("Without a doubt.")
    elif randballnum == 4:
        await ctx.send("Yes – definitely.")
    elif randballnum == 5:
        await ctx.send("You may rely on it.")
    elif randballnum == 6:
        await ctx.send("As I see it, yes.")
    elif randballnum == 7:
        await ctx.send("Most likely.")
    elif randballnum == 8:
        await ctx.send("Outlook good.")
    elif randballnum == 9:
        await ctx.send("Yes.")
    elif randballnum == 10:
        await ctx.send("Signs point to yes.")
    elif randballnum == 11:
        await ctx.send("Reply hazy, try again.")
    elif randballnum == 12:
        await ctx.send("Ask again later.")
    elif randballnum == 13:
        await ctx.send("Better not tell you now.")
    elif randballnum == 14:
        await ctx.send("Cannot predict now.")
    elif randballnum == 15:
        await ctx.send("Concentrate and ask again.")
    elif randballnum == 16:
        await ctx.send("Don't count on it.")
    elif randballnum == 17:
        await ctx.send("My reply is no.")
    elif randballnum == 18:
        await ctx.send("My sources say no.")
    elif randballnum == 19:
        await ctx.send("Outlook not so good.")
    elif randballnum == 20:
        await ctx.send("Very doubtful.")
    else:
        await ctx.send("An error has occurred.")

@bot.command()
async def commands(ctx): #"$Commands" command
    embed = discord.Embed(title="Commands:") #Setting up embed
    embed.add_field(name="$commands: ", value="Billy will show this embed.", inline=False)
    embed.add_field(name="$add (first num) (second num)", value="Billy will add 2 user-specified numbers.", inline=False)
    embed.add_field(name="$subtract (first num) (second num)", value="Billy will subtract 2 user-specified numbers.",
                    inline=False)
    embed.add_field(name="$multiply (first num) (second num)", value="Billy will multiply 2 user-specified numbers.",
                    inline=False)
    embed.add_field(name="$divide (first num) (second num)", value="Billy will divide 2 user-specified numbers. ",
                    inline=True)
    embed.add_field(name="$cool", value="Billy will tell you if you are cool or not.", inline=False)
    embed.add_field(name="$eightball (question)", value="Billy's magic 8-ball will answer all your questions...", inline=False)
    embed.add_field(name="$coinflip", value="Billy will flip a coin for you.", inline=False)
    embed.add_field(name="$cat", value="Billy will provide a random cat image.", inline=False)
    embed.add_field(name="$dog", value="Billy will provide a random dog image.", inline=False)
    embed.add_field(name="$goose", value="Billy will provide a random goose image.", inline=False)
    embed.add_field(name="$waifu", value="Billy will provide a random waifu.", inline=False)
    embed.add_field(name="$lizard", value="Billy will provide a random lizard image.", inline=False)
    embed.add_field(name="$fact", value="Billy will provide a random fact.", inline=False)
    embed.add_field(name='$owoify (your text in "" quotes)', value="Billy will owoify your text.", inline=False)
    embed.add_field(name='$showerthought', value="Billy will provide a thought that you may think while showering.", inline=False)
    embed.set_footer(text="Bot by verbes4#5201 <3")
    await ctx.send(embed=embed)#Bot sends embed

bot.run('put token here') #Bot Token

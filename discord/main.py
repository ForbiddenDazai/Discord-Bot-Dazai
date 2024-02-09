import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("----------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, Ich bin der Sattge bot")

client.run("MTIwNDM3NTczMjE3NjgyMjMyMg.GE5VVx.61BdTQkkNzEe5p7dSca7RrS82bB7tsS-HP1jvU")


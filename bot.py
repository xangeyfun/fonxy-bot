from discord import app_commands, Interaction
from discord.ext import commands
from dotenv import load_dotenv
import discord
import time
import os
import random
import re

load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="", help_command=None, intents=intents, status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="over everyone 👀"))
TOKEN = os.getenv("TOKEN") or ""
meow = re.compile(r"^\**((m+[erao]+[wp]+|n+y+a+|p+u*r+)\**\s*)+~*\s*[.!?]*\s*(:3+)?\**$", re.IGNORECASE)
woof = re.compile(r"^\**((w+[oa]+f+|b+a+r+k+|a+r+f+|w*r+u+f+|a+w+o+)\**\s*)+~*\s*[.!?]*\s*(:3+)?\**$", re.IGNORECASE)

meow_responses = [
    "Meow!",
    "Mew!",
    "Mrow!",
    "Mrrp!",
    "Mrrr!",
    "Purr...",
    "Purrr...",
    "meow :3",
    "mrow :3",
    "mrrp :3",
    "meow meow!!",
    "meow meow meow!",
    "MEOOOOW!!!",
    "MEEEOOOOW!!!",
    "MEOW!!!",
    "MEEEEOW!!!",
    "Mrrrrowww!",
    "Mrrr... meow.",
    "*meows*",
    "M E O W",
    "m e o w :3",
    "meow?",
    "meow!!! :3",
    "meow :333",
    "mrowwww :3",
    "mrrrp! :3",
    "prrrrrr",
    "prrrt!",
    "nya!",
    "nyaa~",
    "nyaa :3",
    "Nya!",
    "Nyaa~",
    "Mew mew!",
    "Mrow mrow!",
    "Meoooow!",
    "Miaow!",
    "Miauu!",
    "Mreow!",
    "Mreow :3",
    "Mrrrow!",
    "Mrrmeow!",
    "mewww :3",
    "meow~",
    "mrow~",
    "mrrp~",
    "purrrr :3",
    "prrrr~",
    "nyaaa!!!",
    "nya :3",
    "nyanyanya!",
    "mew mew!",
    "mew mew mew!",
    "meow meow~",
    "mrow mrow!",
    "mrrp mrrp!",
    "MEOW MEOW!!!",
    "MEEOW!",
    "MEEW!",
    "MRROWWW!!!",
    "MRRRP!",
    "Prrrr!",
    "Prrrp!",
    "Prrr meow!",
    "*mrrps*",
    "*purrs*",
    "*purrs softly*",
    "*meows softly*",
    "*loud meow*",
    "*tiny meow*",
    "meow...",
    "mew...",
    "mrrp?",
    "mrow?",
    "nya?",
    "purrr...",
    "mrrrrp!",
    "mrrrrrow!",
    "mew :333",
    "nyaa~ :3",
    "meow meow meow!!",
    "mrowwwww!",
    "MRAOW!",
    "MRAAAOW!!!",
    "MEOOOW :3",
    "meow!! meow!!",
    "mew~ mew~",
    "nya nya!",
    "nya nya nya!",
    "mrrp~ :3",
    "prrr prrr!",
    "mewp!",
    "meowp!",
    "mrowp!",
    "mreow~",
    "Mrrrmeow!",
    "mewwwww!",
]

woof_responses = [
    "Woof!",
    "Bark!",
    "Arf!",
    "Ruff!",
    "Wruff!",
    "Awoof!",
    "woof :3",
    "arf :3",
    "woof woof!!",
    "WOOF!!!",
    "WOOOOOOF!!!",
    "*woofs*",
    "W O O F",
    "w o o f :3",
    "woof?",
    "woof!!! :3",
    "woof :333",
    "ruff ruff!",
    "arf arf!",
    "AWOOOOOO!",
    "Awooo!",
    "Awooo :3",
    "Wooff!",
    "Wuff!",
    "Wuff wuff!",
    "Wroof!",
    "Rrruff!",
    "Rrruff :3",
    "Borf!",
    "Borf :3",
    "Boof!",
    "Boof boof!",
    "Bwoof!",
    "Bwoof :3",
    "Wouff!",
    "Wouaf!",
    "Aruff!",
    "Arrooo!",
    "Awoooo~",
    "Awooo :333",
    "woooof!",
    "woofff :3",
    "woof~",
    "arf~",
    "ruff~",
    "bork!",
    "bork bork!",
    "bork :3",
    "WOOF WOOF!!!",
    "WOOF WOOF WOOF!",
    "BARK BARK!!!",
    "ARF ARF!",
    "Ruff ruff ruff!",
    "woof woof woof!",
    "wuf wuf!",
    "wuff wuff :3",
    "awoo!",
    "awoooo!",
    "awoooo :3",
    "awoo~",
    "awruff!",
    "grrr woof!",
    "grruff!",
    "ruff?",
    "bork?",
    "boof?",
    "woof...",
    "arf...",
    "ruff...",
    "wuff...",
    "*tiny woof*",
    "*loud bark*",
    "*happy barks*",
    "*woofs softly*",
    "*barks*",
    "*borks*",
    "woof woof~",
    "arf arf :3",
    "ruff ruff :3",
    "bork bork :3",
    "boof boof!",
    "wroof wroof!",
    "WOOF :333",
    "WOOF~",
    "BARK!!!",
    "AROOOO!",
    "AWRROOO!",
    "WOOOORF!",
    "WOOFWOOF!",
    "woof!! woof!!",
    "awoo awoo!",
]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})") # type: ignore
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(f"Error syncing commands: {e}")

    await bot.change_presence(activity=discord.CustomActivity(name="pawing at everyone 24/7"))

@bot.event
async def on_interaction(interaction: Interaction):
    if interaction.type == discord.InteractionType.application_command:
        print(f"Command '/{interaction.data['name']}' invoked by '{interaction.user}' in '{interaction.guild}' (ID: {interaction.guild_id})")
        with open("command_log.txt", "a") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Command '/{interaction.data['name']}' invoked by '{interaction.user}' in '{interaction.guild}' (ID: {interaction.guild_id})\n")
    elif interaction.type == discord.InteractionType.component:
        print(f"Component interaction invoked by '{interaction.user}' in '{interaction.guild}' (ID: {interaction.guild_id})")

@app_commands.allowed_installs(guilds=True, users=False)
@app_commands.allowed_contexts(guilds=True, dms=False, private_channels=False)
@bot.tree.command(name="help", description="Get a list of available commands") #, guild=guild)
async def help(interaction: Interaction):
    help_text = (
        "Here are the available commands:\n"
        "/help - Get a list of available commands\n"
        "/ping - Check the bot's latency\n"
        "/github - Get the bot's GitHub repository link\n"
    )
    await interaction.response.send_message(help_text, ephemeral=True)

@app_commands.allowed_installs(guilds=True, users=False)
@app_commands.allowed_contexts(guilds=True, dms=False, private_channels=False)
@bot.tree.command(name="ping", description="Check the bot's latency") #, guild=guild)
async def ping(interaction: Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"Pong! Latency: {latency}ms", ephemeral=True)

@app_commands.allowed_installs(guilds=True, users=False)
@app_commands.allowed_contexts(guilds=True, dms=False, private_channels=False)
@bot.tree.command(name="github", description="Get the bot's GitHub repository link") #, guild=guild)
async def github(interaction: Interaction):
    await interaction.response.send_message("You can find the bot's source code on GitHub:\nhttps://github.com/xangeyfun/fonxy-bot", ephemeral=True)

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return

    if meow.search(message.content.strip()):
        await message.add_reaction("😼")
        await message.channel.send(random.choice(meow_responses))

    elif woof.search(message.content.strip()):
        await message.add_reaction("🐶")
        await message.channel.send(random.choice(woof_responses))

if __name__ == "__main__":
    bot.run(TOKEN)

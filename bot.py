from discord import app_commands, Interaction
from discord.ext import commands
from dotenv import load_dotenv
import discord
import json
import time
import os
import random
import re

load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="", help_command=None, intents=intents, status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="over everyone 👀"))
TOKEN = os.getenv("TOKEN") or ""
meow = re.compile(r"^\**((m+[erao]+[wp]+|n+y+a+|p+u*r+)s*\**\s*)+~*\s*[.!?]*\s*(:3+)?\**$", re.IGNORECASE)
woof = re.compile(r"^\**((w+[oa]+f+|b+a+r+k+|a+r+f+|w*r+u+f+|a+w+o+)s*\**\s*)+~*\s*[.!?]*\s*(:3+)?\**$", re.IGNORECASE)

with open("reactions.json", "r") as f:
    reactions = json.load(f)
    meow_responses = reactions["meow"]
    woof_responses = reactions["woof"]

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
        print(f"Command '/{interaction.data['name']}' invoked by '{interaction.user}' in '{interaction.guild}'{' (ID: ' + str(interaction.guild_id) + ')' if interaction.guild_id else ''}")
        with open("command_log.txt", "a") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Command '/{interaction.data['name']}' invoked by '{interaction.user}' in '{interaction.guild}'{' (ID: ' + str(interaction.guild_id) + ')' if interaction.guild_id else ''}\n")
    elif interaction.type == discord.InteractionType.component:
        print(f"Component interaction invoked by '{interaction.user}' in '{interaction.guild}'{' (ID: ' + str(interaction.guild_id) + ')' if interaction.guild_id else ''}")

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

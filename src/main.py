import discord
from discord.ext import commands
import os

BOT_TOKEN_PATH = f"{os.path.dirname(os.path.dirname(__file__))}/cred/bot_token"

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    """
    Important: According to the documentation this function is NOT garanteed to
    run first. Womp womp...
    """
    
    # Sync for slash commands
    synced = await client.tree.sync()

    #Will only show up in the host console
    print(f"synced {len(synced)} commands")
    print("Bot is up!")

@client.event
async def on_message(message: discord.message.Message):
    """
    A function that get called when anyone sends a message in the server
    """

    #Does nothing if the bot made a message
    if(message.author == client.user):
        return

@client.tree.command(name="repo", description="Responds with the URL to the repo for the bot")
async def test_command(interaction:discord.Interaction):
    """
    Returns the URL for the Github Repo
    """
    await interaction.response.send_message("Here is the repo:\nhttps://github.com/McTeaCup/DOE23-discord-bot")

with open (BOT_TOKEN_PATH, 'r') as token:
    client.run(token.read())
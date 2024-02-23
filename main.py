import nextcord,asyncio,random,os,sys
from dotenv import find_dotenv,load_dotenv
from nextcord.ext import commands
from nextcord.ext import tasks

sys.dont_write_bytecode = True
load_dotenv(find_dotenv())

client = commands.Bot(
    command_prefix=".",
    help_command=None,
    intents=nextcord.Intents.all()
)

for commands in os.listdir("commands"):
    if commands.endswith(".py"):
        client.load_extension(f"commands.{commands[:-3]}")

for events in os.listdir("events"):
    if events.endswith(".py"):
        client.load_extension(f"events.{events[:-3]}")

@client.event
async def on_ready():
    print("Regpy ready!")

client.run(os.getenv("token"))
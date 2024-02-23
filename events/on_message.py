import nextcord
from nextcord.ext import commands

class on_message(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:pass

        content = message.content
        if content.lower() == "sa" or content.lower() == "hi":
            await message.channel.send(f"Merhaba {message.author.mention} !")

def setup(client):
    client.add_cog(on_message(client))
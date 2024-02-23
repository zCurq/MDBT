# Author: zCurq
# Description: Register bot for Youtube channel

import nextcord,random
import utils.sqlite as sqlite
from nextcord.ext import commands,tasks

class on_ready(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        @tasks.loop(minutes=5) # Saniye için seconds, Saat için hour kullan.
        async def change_presence() -> None:
            statusMessages = [
                "Durum mesajı 1",
                "Durum mesajı 2",
                "Durum mesajı 3"
            ]
            selectedMessage = random.choice(statusMessages)
            await self.client.change_presence(activity=nextcord.Game(name=selectedMessage),status=nextcord.Status.idle)
        await change_presence.start()

def setup(client):
    client.add_cog(on_ready(client))

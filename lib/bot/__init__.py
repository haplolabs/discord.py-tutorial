from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
import discord

PREFIX = "+"
OWNER_IDS = [246508661067743234]

# setup functions
def set_intents():
    intents = discord.Intents.all()
    intents.members = True

    return intents


INTENTS = set_intents()


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.OWNER_IDS = OWNER_IDS
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS, intents=INTENTS)

    def run(self, version, token):
        self.VERSION = version
        self.TOKEN = token

        print(f"running bot {self.VERSION}...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("bot connected")

    async def on_disconnect(self):
        print("bot disconnected")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(785886600441102336)
            print("bot ready")

        else:
            print("bot reconnected")

    async def on_message(self, message):
        pass


bot = Bot()

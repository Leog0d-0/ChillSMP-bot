import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv(".env")
TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    raise ValueError("TOKEN_IS_MISSING")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        print(f"Il bot è online come {self.user}")

    async def setup_hook(self):
        extensions = [
            "cogs.mod",
            "cogs.status"
        ]
        
        for ext in extensions:
            await self.load_extension(ext)
        synced = await self.tree.sync()
        print(f"Comandi slash sincronizzati: {len(synced)}")

bot = Bot()

if __name__ == "__main__":
    bot.run(TOKEN)
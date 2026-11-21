import discord
from discord.ext import commands
from discord import app_commands
import mcstatus

class Player(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="player", description="Vedi quanti player sono online")
    async def player(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True)
        
        server = mcstatus.JavaServer("chill-smp.duckdns.org", 25565)
        
        try:
            status = await server.async_status()
            embed = discord.Embed(
                colour=discord.Color.blurple(),
                title="Player Online",
                description=f"Ci sono **{status.players.online}** player online."
            )
        except Exception as e:
            print(f"Server offline o errore: {e}")
            embed = discord.Embed(
                colour=discord.Color.red(),
                title="Server Offline",
                description=":red_square:Il server è spento:red_square:"
                )
            
        await interaction.followup.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Player(bot))
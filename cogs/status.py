import discord
from discord.ext import commands
from discord import app_commands
import mcstatus

class Status(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @app_commands.command(name="status", description="Vedi se il server è attivo o no")
    async def status(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True)
        
        server = mcstatus.JavaServer("chill-smp.duckdns.org", 25565)
        
        try:
            status = await server.async_status()
            
            embed = discord.Embed(
                colour=discord.Color.green(),
                title="Server Online",
                description=f":green_square:Il server è online:green_square:"
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
    await bot.add_cog(Status(bot))

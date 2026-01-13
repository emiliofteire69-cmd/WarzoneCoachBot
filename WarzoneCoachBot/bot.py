import discord
from discord.ext import commands
import requests
import os
from keep_alive import keep_alive

TOKEN = os.getenv("DISCORD_TOKEN") or "PONE_TU_TOKEN_AQUI"
ACTIVISION_ID = 'guajiritolcuba1010429#psn'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Entrenador Warzone conectado como {bot.user}")

@bot.command(name="estadisticas")
async def estadisticas(ctx):
    url = f"https://api.tracker.gg/api/v2/warzone/standard/profile/psn/{ACTIVISION_ID.replace('#', '%23')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        await ctx.send("No pude obtener tus estadísticas. Verifica que tu perfil esté público.")
        return

    data = res.json()
    try:
        kd = data["data"]["segments"][0]["stats"]["kd"]["displayValue"]
        wins = data["data"]["segments"][0]["stats"]["wins"]["displayValue"]
        await ctx.send(f"📊 **Estadísticas de guajiritolcuba1010429:**\nKD: **{kd}** | Victorias: **{wins}**")
    except:
        await ctx.send("Error al leer tus estadísticas.")

@bot.command(name="entrenador")
async def entrenador(ctx):
    await ctx.send("🎯 **Consejo de WarzoneCoach:**\n1. Baja tu sensibilidad si errás mucho.\n2. Usá UAV siempre que puedas.\n3. No te quedés quieto en zona cerrada.")

keep_alive()
bot.run(TOKEN)
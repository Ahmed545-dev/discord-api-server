from fastapi import FastAPI
import discord
from discord.ext import commands
import asyncio
import threading

app = FastAPI()
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@app.get("/")
def home():
    return {"status": "السيرفر شغال"}

@app.get("/send")
async def send_message(channel_id: int, text: str):
    channel = bot.get_channel(channel_id)
    if channel:
        asyncio.run_coroutine_threadsafe(channel.send(text), bot.loop)
        return {"status": "success"}
    return {"status": "error"}

def run_bot():
    bot.run("YOUR_DISCORD_BOT_TOKEN")

@app.on_event("startup")
async def startup_event():
    threading.Thread(target=run_bot, daemon=True).start()
  

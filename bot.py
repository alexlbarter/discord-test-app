import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

bot = commands.Bot(command_prefix="!")


@bot.command(name="test")
async def test_output(ctx):
    outputs = ["test output 1", "test output 2", "test output 3"]
    response = random.choice(outputs)
    await ctx.send(response)


bot.run(TOKEN)

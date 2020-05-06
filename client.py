import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!\n"
          f"{client.user} is a member of the following servers:")
    for guild in client.guilds:
        print(f"{guild.name} (id: {guild.id})\n"
              f"Members:")
        print_member_max = 10
        count = 0
        for member in guild.members:
            if count < print_member_max:
                print(f"\t- {member.name}#{member.discriminator}")
            else:
                break
            count += 1


client.run(TOKEN)

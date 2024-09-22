import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

class PacepingBot(commands.Bot):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
	async def setup_hook(self):
		await self.load_extension("jishaku") # debugging cog
		await self.load_extension("listeners")
		
bot = PacepingBot(command_prefix=commands.when_mentioned, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Run the bot
import config
bot.run(config.token)

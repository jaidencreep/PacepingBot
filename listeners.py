import discord
from discord.ext import commands

import asyncio

pace_channels = [1009205550187290725, 1009205604008595616, 1009208171384033341]

class Listeners(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.id == self.bot.user.id: return
		# Check if the message is sent in a pace channel
		if message.channel.id in pace_channels:
			# Disable message sending in the channel
			overwrite = message.channel.overwrites_for(message.guild.default_role)
			overwrite.send_messages = False
			await message.channel.set_permissions(message.guild.default_role, overwrite=overwrite)

			# Wait for 5 seconds
			await asyncio.sleep(5)

			# Re-enable message sending in the channel
			overwrite.send_messages = None
			await message.channel.set_permissions(message.guild.default_role, overwrite=overwrite)
	
	@commands.Cog.listener()
	async def on_message_delete(self, message):
		if message.author.id == self.bot.user.id: return
		# Check if the message is sent in a pace channel and make sure it's not a thread creation message, or for whatever reason some other system message (like a pin)
		if message.channel.id in pace_channels and message.type == discord.MessageType.default:
			# Post the contents of the deleted message
			await message.channel.send(
				embed=discord.Embed(
					description=f"### Deleted message by {message.author.mention}\n" + message.content,
					color=int("ff0000", 16)
				),
				allowed_mentions=discord.AllowedMentions.none(),
				silent=True)

async def setup(bot):
	await bot.add_cog(Listeners(bot))

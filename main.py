import os
import random
from hangman import Hangman

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='!')


games_on = {}

@bot.command(name='start', help="Starts the game")
async def start_game(ctx):
	player_id = ctx.__dict__['message'].author.id
	player_mention = ctx.__dict__['message'].author.mention
	
	game = Hangman()
	games_on[player_id] = { "mention": player_mention, "game": game }

	await ctx.send(f'{player_mention} the game has started!\n')
	await ctx.send(game.answer)	
	
		



bot.run(TOKEN)

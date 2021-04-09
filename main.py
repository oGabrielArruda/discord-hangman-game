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
	
	await ctx.send(game.answer + f"\nThere is {game.letters_left} letters left!")

@bot.command(name='clue', help="Attempt of letter")
async def clue(ctx):
	player_id = ctx.__dict__['message'].author.id
	if not games_on.__contains__(player_id):
		await ctx.send("The game isn't started yet! Type !start to begin.")
	
	clue = games_on[player_id]["game"].challenge_object["clue"]
	await ctx.send(f"The clue is: '{clue}'")

@bot.command(name='letter', help="Attempt of letter")
async def letter_attempt(ctx, letter : str):
	player_id = ctx.__dict__['message'].author.id
	if not games_on.__contains__(player_id):
		await ctx.send("The game isn't started yet! Type !start to begin.")

	print(letter)


bot.run(TOKEN)

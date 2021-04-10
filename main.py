import os
import random
import notificator
from hangman import Hangman

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='!')


games_on = {}

@bot.command(name='start', help="Starts the game")
async def start_game(ctx):
	player_id, player_mention = ctx.__dict__['message'].author.id, ctx.__dict__['message'].author.mention
	games_on[player_id] = { "mention": player_mention, "game": Hangman() }
	await notificator.start(ctx, games_on[player_id])

@bot.command(name='clue', help="Attempt of letter")
async def clue(ctx):
	player_id = ctx.__dict__['message'].author.id

	if not games_on.__contains__(player_id):
		await notificator.game_not_started(ctx)
		return
	
	clue = games_on[player_id]["game"].challenge_object["clue"]
	await notificator.clue(ctx, clue)

@bot.command(name='letter', help="Attempt of letter")
async def letter_attempt(ctx, letter : str):
	player_id = ctx.__dict__['message'].author.id
	
	if not games_on.__contains__(player_id):
		await notificator.game_not_started(ctx)
		return

	hangman = games_on[player_id]["game"]

	# verify if letter was already tried
	if letter in hangman.letters_tried:
		await notificator.repeated_letter(ctx, games_on[player_id])
		return

	# verify if the letter exists in the word	
	if hangman.try_letter(letter):
		if hangman.letters_left == 0:
			await notificator.game_won(ctx, games_on[player_id])
			del games_on[player_id]
		else:
			await notificator.correct_letter(ctx, games_on[player_id])
	else:
		if hangman.errors_left == 0:
			await notificator.game_lost(ctx, games_on[player_id])						
			del games_on[player_id]
		else:
			await notificator.missed_letter(ctx, games_on[player_id])

bot.run(TOKEN)

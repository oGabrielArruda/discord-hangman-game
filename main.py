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

	hangman = games_on[player_id]["game"]

	if letter in hangman.letters_tried:
		await print_game(ctx, games_on[player_id], "You already tried this letter!")
		return

	is_correct = hangman.try_letter(letter)
	
	if not is_correct:
		if hangman.errors_left == 0:
			await print_game(ctx, games_on[player_id], 
							f"You lost the game :(\nThe word was {hangman.challenge_object['word']}")						
			del games_on[player_id]
		else:
			await print_game(ctx, games_on[player_id], "You missed!")
	
	if is_correct:
		if hangman.letters_left == 0:
			await print_game(ctx, games_on[player_id], "Congrats!!! You won the game!")
			del games_on[player_id]
		else:
			await print_game(ctx, games_on[player_id], "Oh yea! you got it")

async def print_game(ctx, game_on_object, text):
	player_mention = game_on_object["mention"]
	hangman = game_on_object["game"]

	await ctx.send(
				  f"{player_mention} {text}\n\n" +	
				  f"\nThe word currently formed is {hangman.answer}" + 
				  f"\nThere is {hangman.letters_left} letters left!" +
				  f"\nErrors left: {hangman.errors_left}"
				  f"\nLetters tried: {hangman.letters_tried}")

bot.run(TOKEN)

async def start(ctx, game_on_object):
    start_str = "The game has started! :regional_indicator_g: :regional_indicator_o: :exclamation:"
    await print_game(ctx, game_on_object, start_str)

async def game_not_started(ctx):
    mention = ctx.__dict__['message'].author.mention
    await ctx.send(f"{mention} the game isn't started yet! Type !start to begin.")

async def clue(ctx, clue):
    await ctx.send(f"```fix\nThe clue is: '{clue}' ```")

async def repeated_letter(ctx, game_on_object):
    await print_game(ctx, game_on_object, "You already tried this letter!")

async def missed_letter(ctx, game_on_object):
    await print_game(ctx, game_on_object, "You missed! :x:")

async def correct_letter(ctx, game_on_object):
    await print_game(ctx, game_on_object, "You got it! :white_check_mark:")

async def game_won(ctx, game_on_object):
    await print_game(ctx, game_on_object, "Congrats!!! You won the game! :partying_face:")

async def game_lost(ctx, game_on_object):
    hangman = game_on_object["game"]
    await print_game(ctx, game_on_object, 
							f"You lost the game :sob:\nThe word was ||{hangman.challenge_object['word']}||")



async def print_game(ctx, game_on_object, text):
	player_mention = game_on_object["mention"]
	hangman = game_on_object["game"]

	await ctx.send(
				  f"{player_mention} {text}\n" +	
				  f"\n```yaml\n{hangman.answer}```" + 
				  f"\n```md\n# There is {hangman.letters_left} letters left!" +
				  f"\n# Errors left: {hangman.errors_left} \n```"
				  f"\n```diff\n- Letters tried: {hangman.letters_tried} ```")

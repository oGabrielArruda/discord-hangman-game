import os
import random
from forca import Forca

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='!')


jogos_ocorrendo = {}

@bot.command(name='jogar', help="Inicia o jogo")
async def iniciar_jogo(ctx):
	player_id = ctx.__dict__['message'].author.id
	player_mention = ctx.__dict__['message'].author.mention
	jogo = Forca()

	jogos_ocorrendo[player_id] = { "mention": player_mention, "jogo": jogo }

	await ctx.send(f'{player_mention} jogo iniciado!\n')
	await ctx.send(jogo.answer)	
	
		



bot.run(TOKEN)

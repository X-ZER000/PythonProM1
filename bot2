import discord
import random
from discord.ext import commands
from bot_logic import gen_pass
from settings import settings
from bot_logic import chiste
from bot_logic import flip_coin
from bot_logic import gen_emodji


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def moneda(ctx):
    await ctx.send(flip_coin())

#@bot.command()
#async def chiste(ctx):
    #await ctx.send(chiste())

@bot.command()
async def contar_chiste(ctx): # <-- Cambia el nombre aquí
    await ctx.send(chiste())

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

bot.run(settings["TOKEN"])

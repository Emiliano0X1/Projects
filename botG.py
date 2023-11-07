import discord
import random
from discord.ext import commands
import requests
import json

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)

max_xd=309

@bot.command(name='surprise')
async def surprise(ctx):
   url = 'https://api.thecatapi.com/v1/images/search'
   response = requests.get(url)
   j= response.json()

   if j:
            image_url = j[0].get('url')
            await ctx.send(f'SI tan solo south park hubiera funcionado xd\n{image_url}')
   
@bot.command(name='south')
async def south(ctx):
    random_episode = random.randint(1,max_xd)
    url = f'https://spapi.dev/api/episodes/{random_episode}'
    response = requests.get(url)


    if response.status_code == 200:
        data = response.json()
        episode_name = data['data']['name']
        episode_episode = data['data']['episode']
        episode_season = data['data']['season']
        episode_description = data ['data']['description']
        episode_thumbail = data ['data']['thumbnail_url']

        name = {episode_name}
        episode0= {'episode':episode_episode}
        season={'season': episode_season}
        description={episode_description}
        thumbail = {episode_thumbail}

        await ctx.send(name)
        await ctx.send(season)
        await ctx.send(episode0)
        await ctx.send(description)
        await ctx.send(thumbail)
    else:
        await ctx.send("No jala")

frases = [
    "I want to Jump From This Highway",
    "You can say that adolescence is a hole universally present in the lives of everyone. Large or small, we experience hunger and emptiness in our soul during this period. However, to some boys this hole invades their lives with excessive frequency and in complex form",
    "Messi > Ronaldo",
    "Love is a Lie",
    "May tomorrow begin like a dream",
    "I'll rise above the challenges I face",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "The only way to do great work is to love what you do",
    "You are never too old to set another goal or to dream a new dream.",
    "Should we run away?",
    "Chivas> America",
    "El que escoje , no coje",
    "La vida es como un partido de futbol, entre mas la metes mejor",
    "Leetcode>>>>",
    "jamaica>>>horchata",
    "El que dios lo ayuda, madruga",
    "facts"
    
]

@bot.command()
async def frase(ctx):
    """Muestra una frase aleatoria."""
    frase_aleatoria = random.choice(frases)
    await ctx.send(frase_aleatoria)

@bot.command(name="monday")
async def monday(ctx):
    hora1 = "Introduccion a la Ingenieria (8:00 am a 10:00 am)"
    hora2 = "Calculo Diferencial (10:00 am a 12:00 pm)"
    hora3= "Algebra Lineal (12:00 pm a 2:00 pm)"
    await ctx.send(hora1)
    await ctx.send(hora2)
    await ctx.send(hora3)
   

@bot.command(name="tuesday")
async def tuesday(ctx):
    hora1 = "Metodos de Programacion (8:00 am a 10:00 am)"
    hora2 = "Ser Humano Como Proyecto(10:00 am a 12:00 pm )"
    await ctx.send(hora1)
    await ctx.send(hora2)
    

@bot.command(name="wednesday")
async def wednesday(ctx):
    hora1 = "Calculo Diferencial (10:00 am a 12:00 pm)"
    await ctx.send(hora1)


@bot.command(name="thursday")
async def thursday(ctx):
    hora1 = "Metodos de Programacion (8:00 am a 10:00 am)"
    hora2 = "Ser Humano Como Proyecto(10:00 am a 12:00 pm )"
    await ctx.send(hora1)
    await ctx.send(hora2)

@bot.command(name="friday")
async def friday(ctx):
    hora1 = "Introduccion a la Ingenieria (8:00 am a 10:00 am)"
    hora2 = "Algebra Lineal (12:00 pm a 2:00 pm)"
    await ctx.send(hora1)
    await ctx.send(hora2)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.run(TOKEN)

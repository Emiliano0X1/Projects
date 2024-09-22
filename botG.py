import discord
from discord.ui import View, Select
from dotenv import load_dotenv
import os
import random
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import json

load_dotenv()

TOKEN= os.getenv('BOTG_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)

max_xd=309

@bot.command(name='info',help='Bienvenido, soy BotG')
async def info(ctx):
    embed=discord.Embed(
        title=':book: Menú de Comandos',
        description='Estos son los comandos que contiene BotG',
        color=discord.Colour.red()
    )

    embed.add_field(name='_?frase_',value='Inspira en los momentos dificiles',inline=False)
    embed.add_field(name='?south',value='Entretenimiento puro: un episodio radom de South Park',inline=False)
    embed.add_field(name='?surprise',value='Just Do It',inline=False)
    embed.add_field(name='?(day of a week)',value='Horario de ese dia',inline=False)

    await ctx.send(embed=embed)

@bot.command(name='surprise')
async def surprise(ctx):
   url = 'https://api.thecatapi.com/v1/images/search'
   response = requests.get(url)
   j= response.json()

   if j:
            image_url = j[0].get('url')
            await ctx.send(f'SI tan solo south park hubiera funcionado xd\n{image_url}')


base_urlSP = 'https://www.southpark.lat/episodios'

base_urlEN  = 'https://www.southpark.lat/en/episodes'
class MyView(discord.ui.View):

    def __init__(self,episode_name,episode_season, episode_episode):
        super().__init__(timeout=180.0)
        self.selected_label = None
        self.episode_name = episode_name
        self.episode_season = episode_season
        self.episode_episode = episode_episode

    
    @discord.ui.select(
        placeholder = "Select a Language",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label = "English",
                value = "English",
                description = "Omg this is a great Option, you prefer the original language , GREAT!!"
            ),

            discord.SelectOption(
                label = "Spanish",
                value = "Spanish",
                description = "La neta , el doblaje esta mejor"
            )

        ]
    )


    async def select_callback(self,interaction:discord.Interaction,select : discord.ui.Select):

        await interaction.response.defer()

        self.selected_label = select.values[0]

        print('Ya selecciono los values')
        base_url = base_urlSP if self.selected_label == 'Spanish' else base_urlEN

        response = requests.get(base_url)

        if response.status_code == 200:
            print('El estatus es correcto')
            soup = BeautifulSoup(response.text, 'html.parser')

            episodes = soup.findAll('a', href=True)
            print('Ya tiene los episodios')
            for episode in episodes:
                url_episode = episode['href']
                text_episode = episode.text.lower()

                if f'{self.episode_season}' in text_episode and f'{self.episode_episode}' in text_episode and f'{self.episode_name.lower()}' in text_episode:
            
                    await interaction.followup.send(f"Disponible en {'Español' if self.selected_label == 'Spanish' else 'English'}: {base_url}{url_episode}")
                    break 
        else:
    
            await interaction.followup.send("Error al obtener los episodios. Inténtalo nuevamente.")



   
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

        view = MyView(episode_name=episode_name,episode_season=episode_season,episode_episode=episode_episode)

        await ctx.send("If you want to see free, first Select a Language", view = view)
        print('Procesando')

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
    hora1 = "Analisis de Algoritmos (8:00 am a 10:00 am)"
    hora2 = "Analisis y Modelado de Software (10:00 am a 12:00 pm)"
    await ctx.send(hora1)
    await ctx.send(hora2)
   

@bot.command(name="tuesday")
async def tuesday(ctx):
    hora1 = "Probabilidad (8:00 am a 10:00 am)"
    hora2 = "Dinamica (10:00 am a 12:00 pm )"
    hora3= "Aprendizaje Estrategico (12:00 pm a 2:00 pm)"
    await ctx.send(hora1)
    await ctx.send(hora2)
    await ctx.send(hora3)
    

@bot.command(name="wednesday")
async def wednesday(ctx):
    hora1 = "Analisis de Algoritmos (8:00 am a 10:00 pm)"
    hora2 = "Topicos Selectos de Quimica (10:00 am a 12:00 pm)"
    await ctx.send(hora1)
    await ctx.send(hora2)


@bot.command(name="thursday")
async def thursday(ctx):
    hora1 = "Probabilidad (8:00 am a 10:00 am)"
    hora2 = "Dinamica (10:00 am a 12:00 pm )"
    hora3= "Aprendizaje Estrategico (12:00 pm a 2:00 pm)"
    await ctx.send(hora1)
    await ctx.send(hora2)
    await ctx.send(hora3)

@bot.command(name="friday")
async def friday(ctx):
    hora1 = "Topicos Selectos de Quimica (8:00 am a 10:00 am)"
    hora2 = "Analisis y Modelado de Software (10:00 am a 12:00 pm)"
    await ctx.send(hora1)
    await ctx.send(hora2)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.run(TOKEN)
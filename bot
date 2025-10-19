import discord #Importar libreria de discord
from settings import settings #Importar Clase Settings
from bot_logic import gen_pass #Importar
from bot_logic import chiste
from bot_logic import flip_coin
from bot_logic import gen_emodji

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

#Se imprime cuando se ejecuta correctamente todas las partes
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

#Cada vez que alguien manda un mensaje en un servidor donde está el bot
@client.event
async def on_message(message):
    #Evita que el mensaje tome sus propios mensajes como implimidos por el usuario
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$hola'):
        await message.channel.send("Buenas!~")
    elif message.content.startswith('$Adios') or message.content.startswith('$bye'):
        await message.channel.send("Adios~")
    elif message.content.startswith('$bye'):
        await message.channel.send("Bye~")
    elif message.content.startswith('$Genera un emogi'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$Juguemos a la moneda'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$Cuentame un chiste'):
        await message.channel.send(chiste())
    else:
        await message.channel.send("Your password " + gen_pass(10))

client.run(settings["TOKEN"])

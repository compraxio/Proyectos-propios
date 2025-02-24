import discord
from discord.ext import commands
from Module import recursos_para_manualidades
from Module import Datos_de_contamincacion
from Module import Datos_cientificos_y_consejos
description = 'Una tarea😁'
intenciones = discord.Intents.default()
intenciones.message_content = True
bot = commands.Bot(command_prefix='/', description=description, intents=intenciones)

@bot.event
async def on_ready():
    print(f'Bot listo Hemos iniciado como {bot.user}\n------')

@bot.command(name="Manu", help="Busca manualidades reciclables. Uso: /Manu <Busqueda> [Cantidad=3]")
async def Manu(ctx, *Busqueda: str, Cantidad = 3):
    busqueda = " ".join(Busqueda)
    Resiclaje = recursos_para_manualidades.resiclabe(busqueda, Cantidad)
    await ctx.send(Resiclaje)

@bot.command(name="DataContaA", help="Muestra la calidad del aire en tu ubicación automática. Uso: /DataContaA")
async def DataContaA(ctx):
    Contaminacion = Datos_de_contamincacion.calidad_aire_Ubicacion_Automatica()
    await ctx.send(Contaminacion)
    
@bot.command(name="DataContaM", help="Muestra la calidad del aire en una ciudad específica. Uso: /DataContaM <Ciudad>")
async def DataContaM(ctx,*Ciudad: str):
    try:
        ciudad = " ".join(Ciudad)
        Contaminacion = Datos_de_contamincacion.calidad_aire_Ubicacion_Manual(ciudad)
        await ctx.send(Contaminacion)
    except Exception:
        await ctx.send("No se encontró la ciudad, Por favor intenta con otra.")
@bot.command(name="ContaA", help="Muestra el contaminante dominante en tu ubicación automática. Uso: /ContaA")
async def ContaA(ctx):
    Contaminacion = Datos_de_contamincacion.Contaminante_Dominante_Ubicacion_Automatica()
    await ctx.send(Contaminacion)
    
@bot.command(name="ContaM", help="Muestra el contaminante dominante en una ciudad específica. Uso: /ContaM <Ciudad>")
async def ContaM(ctx,*Ciudad: str):
    try:
        ciudad = " ".join(Ciudad)
        Contaminacion = Datos_de_contamincacion.Contaminante_Dominante_Ubicacion_Manual(ciudad)
        await ctx.send(Contaminacion)
    except Exception:
        await ctx.send("No se encontró la ciudad, Por favor intenta con otra.")
    
@bot.command(name="ClimA", help="Muestra las condiciones actuales del clima en tu ubicación automática. Uso: /ClimA")
async def ClimA(ctx):
    Contaminacion = Datos_de_contamincacion.Condiciones_Actuales_del_Clima_Ubicacion_Automatica()
    await ctx.send(Contaminacion)
    
@bot.command(name="ClimM", help="Muestra las condiciones actuales del clima en una ciudad específica. Uso: /ClimM <Ciudad>")
async def ClimM(ctx,*Ciudad: str):
    try:
        ciudad = " ".join(Ciudad)
        Contaminacion = Datos_de_contamincacion.Condiciones_Actuales_del_Clima_Ubicacion_Manual(ciudad)
        await ctx.send(Contaminacion)
    except Exception:
        await ctx.send("No se encontró la ciudad, Por favor intenta con otra.")

@bot.command(name="Datacien", help="Busca datos científicos sobre un tema. Uso: /Datacien <Dato_cientifico> [cantidad_de_enlaces=3]")
async def Datacien(ctx, *Dato_cientifico: str, cantidad_de_enlaces = 3):
    cato_cientifico = " ".join(Dato_cientifico)
    Dato = Datos_cientificos_y_consejos.Datos_Cientificos(cato_cientifico, cantidad_de_enlaces)
    await ctx.send(Dato)

@bot.command(name="Consejo", help="Busca consejos sobre un tema. Uso: /Consejo <Consejo>")
async def Consejo(ctx, *Consejo: str):
    
    Consejo = Datos_cientificos_y_consejos.Consejos(Consejo)
    await ctx.send(Consejo)

@bot.command(name="Guia", help="Muestra la lista de comandos disponibles.")
async def Guia(ctx):
    guia = "- Comando: Manu\nDescripción: Busca manualidades reciclables. Uso: /Manu <Busqueda> [Cantidad=3]\n- Comando: DataContaA\nDescripción: Muestra la calidad del aire en tu ubicación automática. Uso: /DataContaA\n- Comando: DataContaM\nDescripción: Muestra la calidad del aire en una ciudad específica. Uso: /DataContaM <Ciudad>\n- Comando: ContaA\nDescripción: Muestra el contaminante dominante en tu ubicación automática. Uso: /ContaA\n- Comando: ContaM\nDescripción: Muestra el contaminante dominante en una ciudad específica. Uso: /ContaM <Ciudad>\n- Comando: ClimA\nDescripción: Muestra las condiciones actuales del clima en tu ubicación automática. Uso: /ClimA\n- Comando: ClimM\nDescripción: Muestra las condiciones actuales del clima en una ciudad específica. Uso: /ClimM <Ciudad>\n- Comando: Datacien\nDescripción: Busca datos científicos sobre un tema. Uso: /Datacien <Dato_cientifico> [cantidad_de_enlaces=3]\n- Comando: Consejo\nDescripción: Busca consejos sobre un tema. Uso: /Consejo <Consejo>\n" 
    await ctx.send(guia)

bot.run("Token")

import yt_dlp
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# * Función para asegurar que el directorio existe
def asegurar_directorio(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)

# * Función para seleccionar la carpeta de destino
def seleccionar_carpeta():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    print("Selecciona la carpeta de destino:")
    return filedialog.askdirectory(title="Selecciona la carpeta de destino")

# * Función para descargar un video con la mejor calidad disponible
def descargar_video(link, tipo="mp4"):
    ruta_video = seleccionar_carpeta()
    if not ruta_video:
        print("No se seleccionó ninguna carpeta.")
        return
    asegurar_directorio(ruta_video)

    # Opciones para descargar el video en H.264 (evita problemas con AV1)
    ylp_opts_video = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': f'{ruta_video}/%(title)s.%(ext)s',
        'ffmpeg_location': r"C:/ffmpeg-7.1-essentials_build/bin/ffmpeg.exe",
        'merge_output_format': tipo
    }

    try:
        # Descargar video y audio combinados directamente si es posible
        with yt_dlp.YoutubeDL(ylp_opts_video) as ylp:
            ylp.download([link])

        print("Descarga completa")
        messagebox.showinfo("Descarga Completa", "La descarga ha finalizado.")
    except Exception as e:
        print(f"Hubo un problema al descargar: {e}")

# * Función para descargar solo el audio de un video
def descargar_audio(link, tipo="mp3"):
    ruta_audio = seleccionar_carpeta()
    if not ruta_audio:
        print("No se seleccionó ninguna carpeta.")
        return
    asegurar_directorio(ruta_audio)

    ylp_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{ruta_audio}/%(title)s.{tipo}',
        'postprocessors': [{  
            'key': 'FFmpegExtractAudio',
            'preferredcodec': tipo,  
            'preferredquality': '320' if tipo not in ["wav", "flac", "ogg"] else None
        }],
        'ffmpeg_location': r"C:/ffmpeg-7.1-essentials_build/bin/ffmpeg.exe",
    }

    try:
        with yt_dlp.YoutubeDL(ylp_opts) as ylp:
            ylp.download([link])

        print("Descarga completa")
        messagebox.showinfo("Descarga Completa", "La descarga ha finalizado.")
    except Exception as e:
        print(f"Hubo un problema al descargar: {e}")

# * Función para descargar una lista de reproducción en formato de video
# * Función para descargar una lista de reproducción en formato de video
def descargar_lista_reproduccion_para_video(link, tipo="mp4"):
    ruta_lista_video = seleccionar_carpeta()
    if not ruta_lista_video:
        print("No se seleccionó ninguna carpeta.")
        return
    asegurar_directorio(ruta_lista_video)

    # Opciones de descarga con nombre ordenado
    ylp_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Video + Audio en MP4
        'outtmpl': f'{ruta_lista_video}/%(playlist_index)s - %(title)s.{tipo}',  # Agrega número de orden
        'merge_output_format': tipo,  # Formato final de fusión
        'ffmpeg_location': r"C:/ffmpeg-7.1-essentials_build/bin/ffmpeg.exe",
        'ignoreerrors': True,  # Evita que falle si hay videos privados/eliminados
    }

    try:
        with yt_dlp.YoutubeDL(ylp_opts) as ylp:
            ylp.download([link])

        print("Descarga completa 🎉")
        messagebox.showinfo("Descarga Completa", "Todos los videos han sido descargados exitosamente.")
    except Exception as e:
        print(f"Hubo un problema al descargar la lista de reproducción: {e}")


# * Función para descargar una lista de reproducción en formato de audio
def descargar_lista_reproduccion_para_audio(link, tipo="mp3"):
    ruta_lista_audio = seleccionar_carpeta()
    if not ruta_lista_audio:
        print("No se seleccionó ninguna carpeta.")
        return
    asegurar_directorio(ruta_lista_audio)

    ylp_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{ruta_lista_audio}/%(title)s.{tipo}',
        'ffmpeg_location': r"C:/ffmpeg-7.1-essentials_build/bin/ffmpeg.exe",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': tipo,
            'preferredquality': '320' if tipo not in ["wav", "flac", "ogg"] else None,
        }]
    }

    try:
        with yt_dlp.YoutubeDL(ylp_opts) as ylp:
            ylp.download([link])

        print("Descarga completa")
        messagebox.showinfo("Descarga Completa", "La descarga ha finalizado.")
    except Exception as e:
        print(f"Hubo un problema al descargar: {e}")

# * Bucle principal para interactuar con el usuario
while True:
    pregunta = input("¿Desea descargar un video, un audio o una lista de reproducción? (video/audio/lista):\n").strip().lower()

    if pregunta == "video":
        link = input("Ingrese el link del video:\n").strip()
        tipo = input("Ingrese el formato de descarga (MP4, MKV, AVI, MOV, WEBM):\n").strip().lower()
        descargar_video(link, tipo)

    elif pregunta == "audio":
        link = input("Ingrese el link del video para extraer el audio:\n").strip()
        tipo = input("Ingrese el formato de descarga (MP3, WAV, AAC, FLAC, OGG):\n").strip().lower()
        descargar_audio(link, tipo)

    elif pregunta == "lista":
        pregunta2 = input("¿Desea descargar la lista de reproducción en video o audio? (video/audio):\n").strip().lower()

        if pregunta2 == "video":
            link = input("Ingrese el link de la lista de reproducción de videos:\n").strip()
            tipo = input("Ingrese el formato de descarga (MP4, MKV, AVI, MOV, WEBM):\n").strip().lower()
            descargar_lista_reproduccion_para_video(link, tipo)

        elif pregunta2 == "audio":
            link = input("Ingrese el link de la lista de reproducción de audios:\n").strip()
            tipo = input("Ingrese el formato de descarga (MP3, WAV, AAC, FLAC, OGG):\n").strip().lower()
            descargar_lista_reproduccion_para_audio(link, tipo)

    # * Pregunta si el usuario desea continuar o salir
    continuar = input("¿Desea realizar otra descarga? (si/no):\n").strip().lower()
    if continuar != "si":
        break

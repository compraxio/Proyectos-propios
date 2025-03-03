import yt_dlp

# * Función para descargar un video con la mejor calidad disponible
def descargar_video(link, tipo="mp4"):
    ylp_opts = {
        'format': 'bestvideo+bestaudio/best',  # * Descarga la mejor calidad de video con audio
        'outtmpl': f'C:/Users/luis angel/OneDrive/Escritorio/Descargar/videos/%(title)s.%(ext)s',  # * Ruta de almacenamiento
        'merge_output_format': tipo,  # * Formato final del video descargado
        'ffmpeg_location': r"C:/ffmpeg-7.1-essentials_build/bin/ffmpeg.exe",  # * Ruta del ejecutable de FFmpeg
        'postprocessors': [{ 'key': 'FFmpegMerger' }],  # * Une el audio y el video descargado
    }
    try:
        with yt_dlp.YoutubeDL(ylp_opts) as ylp:
            ylp.download([link])
        print("Descarga completa")
    except Exception as e:
        print(f"Hubo un problema al descargar: {e}")

# * Función para descargar solo el audio de un video
def descargar_audio(link, tipo="mp3"):
    ylp_opts = {
        'format': 'bestaudio/best',  # * Descarga la mejor calidad de audio disponible
        'outtmpl': f'C:/Users/luis angel/OneDrive/Escritorio/Descargar/Audios/%(title)s.{tipo}',
        'postprocessors': [{  # * Extrae el audio del archivo descargado
            'key': 'FFmpegExtractAudio',
            'preferredcodec': tipo,  # * Codec de audio preferido (MP3, WAV, FLAC, etc.)
            'preferredquality': None if tipo in ["wav", "flac", "ogg"] else '320',  # * Calidad 320kbps (excepto en formatos sin pérdida)
        }],
        'ffmpeg_location': r"C:/ffmpeg-7.1-essentials_build/bin/ffmpeg.exe",
    }
    try:
        with yt_dlp.YoutubeDL(ylp_opts) as ylp:
            ylp.download([link])
        print("Descarga completa")
    except Exception as e:
        print(f"Hubo un problema al descargar: {e}")

# * Función para descargar una lista de reproducción en formato de video
def descargar_lista_reproduccion_para_video(link, tipo="mp4"):
    ylp_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'C:/Users/luis angel/OneDrive/Escritorio/Descargar/listas de reproduccion/%(playlist_title)s/video/%(title)s.{tipo}',
        'merge_output_format': tipo,
        'ffmpeg_location': r"C:/ffmpeg-7.1-essentials_build/bin/ffmpeg.exe",
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': tipo,
        }]
    }
    try:
        with yt_dlp.YoutubeDL(ylp_opts) as ylp:
            ylp.download([link])
        print("Descarga completa")
    except Exception as e:
        print(f"Hubo un problema al descargar: {e}")

# * Función para descargar una lista de reproducción en formato de audio
def descargar_lista_reproduccion_para_audio(link, tipo="mp3"):
    ylp_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'C:/Users/luis angel/OneDrive/Escritorio/Descargar/listas de reproduccion/%(playlist_title)s/audio/%(title)s.{tipo}',
        'ffmpeg_location': r"C:/ffmpeg-7.1-essentials_build/bin/ffmpeg.exe",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': tipo,
            'preferredquality': None if tipo in ["wav", "flac", "ogg"] else '320',
        }]
    }
    try:
        with yt_dlp.YoutubeDL(ylp_opts) as ylp:
            ylp.download([link])
        print("Descarga completa")
    except Exception as e:
        print(f"Hubo un problema al descargar: {e}")

# * Bucle principal para interactuar con el usuario
while True:
    pregunta = input("¿Desea descargar un video, un audio o una lista de reproduccion? (video/audio/lista):\n").strip().lower()
    
    if pregunta == "video":
        link = input("Ingrese el link del video:\n").strip()
        tipo = input("Ingrese el formato de descarga (MP4, MKV, AVI, MOV, WEBM):\n").strip().lower()
        if tipo == "mp4":
            print("Se recomienda descargar el audio y el video por separado para evitar problemas de sincronización.")
            descargar_video(link, tipo)
        else:
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
            if tipo == "mp4":
                print("Se recomienda descargar el audio y el video por separado para evitar problemas de sincronización.")
                descargar_lista_reproduccion_para_video(link, tipo)
            else:
                descargar_lista_reproduccion_para_video(link, tipo)
        
        elif pregunta2 == "audio":
            link = input("Ingrese el link de la lista de reproducción de audios:\n").strip()
            tipo = input("Ingrese el formato de descarga (MP3, WAV, AAC, FLAC, OGG):\n").strip().lower()
            descargar_lista_reproduccion_para_audio(link, tipo)
    
    # * Pregunta si el usuario desea continuar o salir
    continuar = input("¿Desea realizar otra descarga? (si/no):\n").strip().lower()
    if continuar != "si":
        break

import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog

# Inicializar la interfaz de tkinter
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Permitir al usuario seleccionar archivos de audio
print("Selecciona los archivos de audio")
archivo = filedialog.askopenfilenames(title="Selecciona los archivos de audio", filetypes=[("Audio Files", "*.wav")])

# Permitir al usuario seleccionar el directorio de salida
print("Selecciona el directorio de guardado")
output_directory = filedialog.askdirectory(title="Selecciona el directorio de guardado")

# Crear una instancia del reconocedor de voz
r = sr.Recognizer()

# Iterar sobre cada archivo de la lista
for au in archivo:
    output_file = f"{output_directory}/{au.split('/')[-1]}.txt"  # Nombre del archivo de salida para la transcripción
    print(f"Procesando archivo {au}")

    try:
        # Abrir el archivo de audio
        with sr.AudioFile(au) as source:
            # Obtener la duración del audio
            duration = int(source.DURATION)
            # Variable para almacenar la transcripción completa
            full_text = ""

            try:
                estimacion_de_fragmentos = duration // 10
                print(f"Procesando archivo... este durará {estimacion_de_fragmentos} fragmentos")
            except Exception:
                print("No se pudo estimar la cantidad de fragmentos")

            # Procesar el audio en fragmentos de 10 segundos
            for i in range(0, duration, 10):
                try:
                    # Capturar un fragmento de audio de 10 segundos
                    audio_data = r.record(source, duration=10)
                    # Convertir el audio a texto usando Google Speech Recognition
                    text = r.recognize_google(audio_data, language="es-ES")
                    # Agregar el texto reconocido a la transcripción completa
                    full_text += text + "\n"
                    print(f"Fragmento {i // 10 + 1}: {text}")
                except sr.UnknownValueError:
                    # Manejar el caso en que el audio no se pueda entender
                    print(f"Fragmento {i // 10 + 1}: No se pudo entender el audio.")
                    full_text += "[No se pudo entender el audio]\n"
                except sr.RequestError as e:
                    # Manejar errores de comunicación con el servicio de Google
                    print(f"Error al comunicarse con el servicio de Google: {e}")
                    break

            # Guardar la transcripción completa en un archivo de texto
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(full_text)

            print(f"Transcripción guardada y completada en {output_file}")
    except FileNotFoundError:
        # Manejar el caso en que el archivo de audio no se encuentre
        print(f"El archivo {au} no se encontró. Asegúrate de que el archivo exista")
    except ValueError as e:
        # Manejar errores relacionados con el archivo de audio
        print(f"Error con el archivo de audio: {e}")
    except Exception as e:
        # Manejar cualquier otro error inesperado
        print(f"Ocurrió un error inesperado: {e}")

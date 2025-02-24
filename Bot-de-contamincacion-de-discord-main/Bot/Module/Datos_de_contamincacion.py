import requests
Token = "cf5e416560a196663f6af1ce80c56b68c056f2a1"

def calidad_aire_Ubicacion_Automatica():
    Token = "cf5e416560a196663f6af1ce80c56b68c056f2a1"
    url = f"https://api.waqi.info/feed/here/?token={Token}"
    response = requests.get(url)
    if response.status_code != 200:
        return "Error en la solicitud"
    data = response.json()
    Calidad_del_aire = data['data']['aqi']
    if Calidad_del_aire >= 0 and Calidad_del_aire <= 50:
        Ciudad = data['data']['city']['name']
        return f"la calidad del aire en {Ciudad} es {Calidad_del_aire} y es considerada Buena"
    elif Calidad_del_aire >= 50 and Calidad_del_aire <= 100:
        Ciudad = data['data']['city']['name']
        return f"la calidad del aire en {Ciudad} es {Calidad_del_aire} y es considerada Regular"
    elif Calidad_del_aire >= 100 and Calidad_del_aire <= 150:
        Ciudad = data['data']['city']['name']
        return f"la calidad del aire en {Ciudad} es {Calidad_del_aire} y es considerada Poco saludable"
    elif Calidad_del_aire >= 150 and Calidad_del_aire <= 200:
        Ciudad = data['data']['city']['name']
        return f"la calidad del aire en {Ciudad} es {Calidad_del_aire} y es considerada Insalubre"
    elif Calidad_del_aire >= 200 and Calidad_del_aire <= 300:
        Ciudad = data['data']['city']['name']
        return f"la calidad del aire en {Ciudad} es {Calidad_del_aire} y es considerada Muy insalubre"
    elif Calidad_del_aire >= 300:
        Ciudad = data['data']['city']['name']
        return f"la calidad del aire en {Ciudad} es {Calidad_del_aire} y es considerada Peligrosa"
def calidad_aire_Ubicacion_Manual(Ciudad):
    Token = "cf5e416560a196663f6af1ce80c56b68c056f2a1"
    url = f"https://api.waqi.info/feed/{Ciudad}/?token={Token}"
    response = requests.get(url)
    if response.status_code != 200:
        return "Error en la solicitud"
    data = response.json()
    Calidad_del_aire = data['data']['aqi']
    if Calidad_del_aire >= 0 and Calidad_del_aire <= 50:
        Ciudad = data['data']['city']['name']
        return f"la calidad del aire en {Ciudad} es {Calidad_del_aire} y es considerada Buena"
    elif Calidad_del_aire >= 50 and Calidad_del_aire <= 100:
        Ciudad = data['data']['city']['name']
        return f"la calidad del aire en {Ciudad} es {Calidad_del_aire} y es considerada Regular"
    elif Calidad_del_aire >= 100 and Calidad_del_aire <= 150:
        Ciudad = data['data']['city']['name']
        return f"la calidad del aire en {Ciudad} es {Calidad_del_aire} y es considerada Poco saludable"
    elif Calidad_del_aire >= 150 and Calidad_del_aire <= 200:
        Ciudad = data['data']['city']['name']
        return f"la calidad del aire en {Ciudad} es {Calidad_del_aire} y es considerada Insalubre"
    elif Calidad_del_aire >= 200 and Calidad_del_aire <= 300:
        Ciudad = data['data']['city']['name']
        return f"la calidad del aire en {Ciudad} es {Calidad_del_aire} y es considerada Muy insalubre"
    elif Calidad_del_aire >= 300:
        Ciudad = data['data']['city']['name']
        return f"la calidad del aire en {Ciudad} es {Calidad_del_aire} y es considerada Peligrosa"
    
def Contaminante_Dominante_Ubicacion_Automatica():
    Token = "cf5e416560a196663f6af1ce80c56b68c056f2a1"
    url = f"https://api.waqi.info/feed/here/?token={Token}"
    response = requests.get(url)
    if response.status_code != 200:
        return "Error en la solicitud"
    data = response.json()
    Ciudad = data['data']['city']['name']
    Contaminante = data['data']['dominentpol']
    return f"El contaminante dominante en {Ciudad} es {Contaminante} este contaminante es el que tiene el mayor impacto en la calidad del aire por lo que es importante tenerlo en cuenta"
def Contaminante_Dominante_Ubicacion_Manual(Ciudad):
    Token = "cf5e416560a196663f6af1ce80c56b68c056f2a1"
    url = f"https://api.waqi.info/feed/{Ciudad}/?token={Token}"
    response = requests.get(url)
    if response.status_code != 200:
        return "Error en la solicitud"
    data = response.json()
    Ciudad = data['data']['city']['name']
    Contaminante = data['data']['dominentpol']
    return f"El contaminante dominante en {Ciudad} es {Contaminante} este contaminante es el que tiene el mayor impacto en la calidad del aire por lo que es importante tenerlo en cuenta"

def Condiciones_Actuales_del_Clima_Ubicacion_Automatica():
    Token = "cf5e416560a196663f6af1ce80c56b68c056f2a1"
    url = f"https://api.waqi.info/feed/here/?token={Token}"
    response = requests.get(url)
    if response.status_code != 200:
        return "Error en la solicitud"
    data = response.json()
    Ciudad = data['data']['city']['name']
    punto_de_rocio = data['data']['iaqi']['dew']['v']
    Humedad = data['data']['iaqi']['h']['v']
    Presión_atmosférica = data['data']['iaqi']['p']['v']
    PM25 = data['data']['iaqi']['pm25']['v']
    Temperatura = data['data']['iaqi']['t']['v']
    Velocidad_del_viento = data['data']['iaqi']['w']['v']
    return f"Las condiciones actuales del clima en {Ciudad} son:\nPunto de rocio: {punto_de_rocio}°C\nHumedad: {Humedad}%\nPresión atmosférica: {Presión_atmosférica}hPa\nPM25: {PM25}µg/m³\nTemperatura: {Temperatura}°C\nVelocidad del viento: {Velocidad_del_viento}m/s"

def Condiciones_Actuales_del_Clima_Ubicacion_Manual(Ciudad):
    Token = "cf5e416560a196663f6af1ce80c56b68c056f2a1"
    url = f"https://api.waqi.info/feed/{Ciudad}/?token={Token}"
    response = requests.get(url)
    if response.status_code != 200:
        return "Error en la solicitud"
    data = response.json()
    Ciudad = data['data']['city']['name']
    punto_de_rocio = data['data']['iaqi']['dew']['v']
    Humedad = data['data']['iaqi']['h']['v']
    Presión_atmosférica = data['data']['iaqi']['p']['v']
    PM25 = data['data']['iaqi']['pm25']['v']
    Temperatura = data['data']['iaqi']['t']['v']
    Velocidad_del_viento = data['data']['iaqi']['w']['v']
    return f"Las condiciones actuales del clima en {Ciudad} son:\nPunto de rocio: {punto_de_rocio}°C\nHumedad: {Humedad}%\nPresión atmosférica: {Presión_atmosférica}hPa\nPM25: {PM25}µg/m³\nTemperatura: {Temperatura}°C\nVelocidad del viento: {Velocidad_del_viento}m/s"

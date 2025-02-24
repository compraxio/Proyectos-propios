from serpapi import GoogleSearch
def Datos_Cientificos(Dato_cientifico, cantidad_de_enlaces):  # sourcery skip: use-named-expression
    params = {
        "q": f"Datos Cientificos de la{Dato_cientifico}",  # Consulta de búsqueda
        "location": "Mexico City, Mexico",  # Ubicación específica
        "hl": "es",  # Idioma (en = inglés)
        "gl": "mx",  # Código del país (us = Estados Unidos)
        "google_domain": "google.com.mx",  # Dominio de Google
        "api_key": "c4ea6b07cbade43b7a7c7955016ffc9463975b858b0ccb50863bdc57e40bf1c8"  # ¡Sustituye esto con tu clave API de SerpAPI!
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    resultados_organicos=results.get('organic_results', [])

    if len(resultados_organicos) == 0:
        return "No se encontraron resultados"
    enlaces = ""
    for results in resultados_organicos[:cantidad_de_enlaces]:
        titulo = results.get('title', None)
        enlace = results.get('link', None)
        if enlace and titulo is not None:
            enlaces += f"{titulo} : {enlace}\n"
    return enlaces

def Consejos(Consejo):  # sourcery skip: use-named-expression
    params = {
        "q": f"Consejos para {Consejo}",  # Consulta de búsqueda
        "location": "Mexico City, Mexico",  # Ubicación específica
        "hl": "es",  # Idioma (en = inglés)
        "gl": "mx",  # Código del país (us = Estados Unidos)
        "google_domain": "google.com.mx",  # Dominio de Google
        "api_key": "c4ea6b07cbade43b7a7c7955016ffc9463975b858b0ccb50863bdc57e40bf1c8"  # ¡Sustituye esto con tu clave API de SerpAPI!
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    resultados_organicos=results.get('related_questions', [])

    if len(resultados_organicos) == 0:
        return "No se encontraron resultados"
    enlaces = ""
    for results in resultados_organicos[:4]:
        titulo = results.get('title', None)
        lista = results.get('list', None)
        if lista and titulo is not None:
            enlaces += f"{titulo} : {lista}\n"
    return enlaces

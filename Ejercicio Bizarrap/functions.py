from data import lista_bzrp

def obtener_titulo():
    for tema in lista_bzrp:
        nombre_tema = tema["title"]
        print(nombre_tema)

def obtener_titulo_views():
    for tema in lista_bzrp:
        nombre_tema = tema["title"]
        views_tema = tema["views"]
        print(f"Nombre: {nombre_tema} | Visualizaciones: {views_tema}")


def obtener_maximo_views():
    tema_max_views = lista_bzrp[0]["views"]
    for tema in lista_bzrp:
        if tema["views"]> tema_max_views:
            tema_max_views = tema["views"]
            nombre_max_views = tema["title"]

    print(f"Titulo: {nombre_max_views} | Visualizaciones: {tema_max_views} ")


def obtener_minimo_views():
    tema_min_views = lista_bzrp[0]["views"]
    for tema in lista_bzrp:
        if tema["views"]< tema_min_views:
            tema_min_views = tema["views"]
            nombre_min_views = tema["title"]

    print(f"Titulo: {nombre_min_views} | Visualizaciones: {tema_min_views} ")


def acumular_views():
    contar_views = 0
    for tema in lista_bzrp:
        contar_views += tema["views"]
    print(f"Cantidad total de reproducciones: {contar_views}")


def obtener_promedio_views():
    contar_views = 0
    contar_temas = len(lista_bzrp)
    for tema in lista_bzrp:
        contar_views += tema["views"]

    promedio_views = contar_views / contar_temas
    print(f"El promedio de visualizaciones es: {promedio_views:.0f}")


def obtener_min_max_duracion():
    min_duracion = lista_bzrp[0]["length"]
    max_duracion = lista_bzrp[0]["length"]

    for tema in lista_bzrp:
        if tema["length"] < min_duracion:
            min_duracion = tema["length"]
            nombre_min_duracion = tema["title"]

        elif tema["length"] > max_duracion:
            max_duracion = tema["length"]
            nombre_max_duracion = tema["title"]

    print(f"Cancion con menos duracion {nombre_min_duracion} | Duracion del tema: {min_duracion} segundos.\nCancion con mas duracion: {nombre_max_duracion} | Duracion del tema: {max_duracion} segundos.")




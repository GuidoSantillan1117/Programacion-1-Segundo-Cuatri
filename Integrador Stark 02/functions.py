from data_stark import lista_personajes
def obtener_nombre_segun_genero(lista:list):
    for heroe in lista:
        if heroe["genero"] == "NB":
            print(heroe["nombre"])
            
def obtener_min_max_atributo(lista:list,genero:str,filtro:str,filtro_atributo:str):
    filtro_mas_alto = False
    filtro_mas_bajo = False

    nombre = ""

    max_atributo = 0
    min_atributo = 10000000

    for heroe in lista:
        atributo = float(heroe[filtro_atributo])
        if heroe["genero"] == genero:
            if filtro == "mayor":
                filtro_mas_alto = True
            elif filtro == "menor":
                filtro_mas_bajo = True
            
            if filtro_mas_alto:
                if atributo>max_atributo:
                    max_atributo = atributo
                    nombre = heroe["nombre"]

            elif filtro_mas_bajo:
                if atributo<min_atributo:
                    min_atributo = atributo
                    nombre = heroe["nombre"]

    print(f"El superheroe con {filtro} {filtro_atributo} del genero {genero} es : {nombre}")

def obtener_promedio_fuerza(lista:list):
    acumular_fuerza = 0
    contador_genero_nb = 0
    for heroe in lista:
        fuerza = float(heroe["fuerza"])
        if heroe["genero"] == "NB":
            acumular_fuerza += fuerza
            contador_genero_nb += 1

    promedio_fuerza = acumular_fuerza / contador_genero_nb

    print(f"La fuerza promedio de los superheroes con genero NB es: {promedio_fuerza:.2f}")

def contar_heroes_color_atributo(lista:list,atributo:str):
    diccionario = {}
    for heroe in lista:
        if atributo in heroe:
            valor = heroe[atributo]
            if valor in diccionario:
                diccionario[valor] += 1
            else:
                diccionario[valor] = 1

    return diccionario


def agrupar_heroe_segun_atributo(lista:list,atributo:str):
    diccionario = {}
    for heroe in lista:
        if atributo in heroe:
            valor = heroe[atributo]
            nombre = heroe["nombre"]
            if len(valor) <1:
                valor = "none"

            if valor in diccionario:
                diccionario[valor] += f"  {nombre}"
            else:
                diccionario[valor] = f"{nombre}"
            

    return diccionario
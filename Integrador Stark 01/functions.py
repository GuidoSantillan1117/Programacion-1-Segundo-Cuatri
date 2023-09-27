from data_stark import lista_personajes

def obtener_datos_lista(lista:list):
    for heroe in lista:
        print(heroe)
        

def obtener_dato_max_fuerza(lista:list):
    max_fuerza = lista[0]["fuerza"]
    for heroe in lista:
        if heroe["fuerza"] > max_fuerza:
            max_fuerza = heroe["fuerza"]
            identidad_max_fuerza = heroe["identidad"]
            peso_max_fuerza = float(heroe["peso"])

    print(f"Identidad del heroe más fuerte: {identidad_max_fuerza} | Peso: {peso_max_fuerza:.2f}")

def obtener_dato_min_altura(lista:list):
    min_altura = lista[0]["altura"]
    for heroe in lista:
        if heroe["altura"]<min_altura:
            min_altura = heroe["altura"]
            nombre_min_altura = heroe["nombre"]
            identidad_min_altura = heroe["identidad"]

    print(f"Nombre del heroe más bajo: {nombre_min_altura} | Identidad: {identidad_min_altura}")

def obtener_promedio_peso_masculinos(lista:list):
    acumular_peso_masculino = 0
    heroes_masculinos = 0
    for heroe in lista:
        if heroe["genero"] == "M":
            heroes_masculinos += 1
            acumular_peso_masculino += float(heroe["peso"])

    promedio_peso = acumular_peso_masculino / heroes_masculinos

    print(f"Peso promedio de los superheroes masculinos: {promedio_peso:.2f} KG")

def obtener_heroes_fuerza_superior_femeninos(lista:list):
    acumular_fuerza_femenino = 0
    heroes_femeninos = 0
    
    for heroe in lista:
        if heroe["genero"] == "F":
            heroes_femeninos +=1
            acumular_fuerza_femenino += float(heroe["fuerza"])

    promedio_fuerza_femenino = acumular_fuerza_femenino / heroes_femeninos

    for heroe in lista:
        if float(heroe["fuerza"]) > promedio_fuerza_femenino:
            nombre_fuerza_superior = heroe["nombre"]
            peso_fuerza_superor = float(heroe["peso"])
            print(f"Nombre del personaje con mayor fuerza que el promedio femenino: {nombre_fuerza_superior} | Peso: {peso_fuerza_superor:.2f} KG")
            


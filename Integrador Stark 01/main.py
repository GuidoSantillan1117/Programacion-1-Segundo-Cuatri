from functions import * 
from data_stark import lista_personajes

def mostrar_menu():
    seguir = True
    while seguir:
        menu = ["----------------------------------------------------------",
            "1. Datos de todos los heroes","2. Identidad y peso del heroe mas fuerte","3. Nombre e identidad del heroe mas bajo","4. Peso promedio de los heroes",
            "5. Nombre y peso de los heroes con fuerza mayor al promedio del de los femeninos","\n6. Salir"]

        for opcion in menu:
            print(opcion)

        respuesta = int(input("Ingrese una opción: "))

        match respuesta:
            case 1:
                obtener_datos_lista(lista_personajes)
            case 2:
                obtener_dato_max_fuerza(lista_personajes)
            case 3:
                obtener_dato_min_altura(lista_personajes)
            case 4:
                obtener_promedio_peso_masculinos(lista_personajes)
            case 5:
                obtener_heroes_fuerza_superior_femeninos(lista_personajes)
            case 6:
                seguir = False

mostrar_menu()


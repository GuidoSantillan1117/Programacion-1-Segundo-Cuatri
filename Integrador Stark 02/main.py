from functions import * 
from data_stark import lista_personajes

def mostrar_menu():
    seguir = True
    while seguir:
        menu = ["----------------------------------------------------------",
            "1. Datos de todos los heroes","2. Mostrar superheroes con menor o mayor atributo (Altura o Fuerza) segun su genero (F,M o NB)","3. Mostrar fuerza promedio del genero NB"
            ,"4. Mostrar todos los heroes listados segun el color de su atributo (Color de pelo o de ojos)",
            "5. Listar heroes agrupado por su atributo (Color de ojos o inteligencia)","\n6. Salir"]

        for opcion in menu:
            print(opcion)

        respuesta = int(input("Ingrese una opción: "))

        match respuesta:
            case 1:
                obtener_nombre_segun_genero(lista_personajes)
            case 2:
                respuesta_filtro_atributo = input("Ingrese el atributo por el cual desea filtrar (altura o fuerza): ")
                while respuesta_filtro_atributo != "altura" and respuesta_filtro_atributo != "fuerza":
                    respuesta_filtro_atributo = input("Reingrese el atributo por el cual desea filtrar (altura o fuerza): ")
                respuesta_genero = input("Ingrese el genero por el cual quiere buscar (F,M o NB): ")
                while respuesta_genero != "F" and respuesta_genero != "M" and respuesta_genero!= "NB":
                    respuesta_genero = input("Reingrese el genero por el cual quiere buscar (F,M o NB): ")
                respuesta_filtro = input("Ingrese por que caracteristica quiere filtar,escriba (menor) para el mas bajo y (mayor) para el mas alto. ")
                while respuesta_filtro != "menor" and respuesta_filtro != "mayor":
                    respuesta_filtro = input("Reingrese por que caracteristica quiere filtar,escriba (menor) para el mas bajo y (mayor) para el mas alto. ")
                obtener_min_max_atributo(lista_personajes,respuesta_genero,respuesta_filtro,respuesta_filtro_atributo)
            case 3:
                obtener_promedio_fuerza(lista_personajes)
            case 4:
                respuesta_color_atributo = input("Ingrese el atributo del cual quiere ver el conteo de los superheroes segun sus colores, escriba (color_ojos) para el de los ojos y (color_pelo) para el del pelo: ")
                while respuesta_color_atributo != "color_ojos" and respuesta_color_atributo != "color_pelo":
                    respuesta_color_atributo = input("Reingrese el atributo del cual quiere ver filtrado por sus colores, escriba (color_ojos)para el de los ojos y (color_pelo)para el del pelo: ")
                mostrar = contar_heroes_color_atributo(lista_personajes,respuesta_color_atributo)
                print(mostrar)
            case 5:
                respuesta_filtro_atributos = input("Ingrese un atributo por el cual agrupar,escriba (color_ojos) para agrupar por el color de los ojos o (inteligencia) para agrupar por su inteligencia: ")
                while respuesta_filtro_atributos != "color_ojos" and respuesta_filtro_atributos != "inteligencia":
                    respuesta_filtro_atributos = input("Reingrese un atributo por el cual agrupar,escriba (color_ojos) para agrupar por el color de los ojos o (inteligencia) para agrupar por su inteligencia: ")
                mostrar = agrupar_heroe_segun_atributo(lista_personajes,respuesta_filtro_atributos)
                print(mostrar)
            case 6:
                seguir = False

mostrar_menu()
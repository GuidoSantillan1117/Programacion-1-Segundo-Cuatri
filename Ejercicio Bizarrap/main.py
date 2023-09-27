from functions import * 

def mostrar_menu():
    seguir = True
    while seguir:
        menu = ["----------------------------------------------------------",
            "1. Titulo de todas las canciones.","2. Titulo de todas las canciones y sus reproducciones.","3. Tema con mas visualizaciones.","4. Tema con menos visualizaciones.",
                "5. Cantidad total de visualizaciones", "6. Promedio de reproducciones.","7. Canción con menor y mayor duración.","\n \n8. Salir","----------------------------------------------------------",]

        for opcion in menu:
            print(opcion)

        respuesta = int(input("Ingrese una opción: "))

        match respuesta:
            case 1:
                obtener_titulo()
            case 2:
                obtener_titulo_views()
            case 3:
                obtener_maximo_views()
            case 4:
                obtener_minimo_views()
            case 5:
                acumular_views()
            case 6:
                obtener_promedio_views()
            case 7:
                obtener_min_max_duracion()
            case 8:
                seguir= False


mostrar_menu()
            



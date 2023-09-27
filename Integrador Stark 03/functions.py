from data_stark import *

def stark_normalizar_datos(lista:list):
    """
    Brief:
    Normaliza los datos de la lista de personajes,validando que no se encuentre vacia y casteando los valores numericos de strings a float o int.
    Si los datos fueron normalizados o no se le notifica esto al usuario en su llamada.

    Parametro/s:
    La lista la cual normalizara

    Return:
    Devuelve un valor booleano True o False para verificar si estos datos fueron normalizados.

    """
    datos_modificados = False
    if len(lista)>0:
        for personaje in lista:
            if type(personaje["fuerza"]) != float:
                personaje["fuerza"]= float(personaje["fuerza"])
                datos_modificados = True
            if type(personaje["peso"]) != float:
                personaje["peso"]= float(personaje["peso"])
                datos_modificados = True
            if type(personaje["altura"]) != float:
                personaje["altura"]= float(personaje["altura"])
                datos_modificados = True
                
        if datos_modificados:
            print("Datos normalizados correctamente.")
        else:
            print("Hubo un error al normalizar los datos. Verifique que los datos ya no se hayan normalizado anteriormente.")
    

    else:
        print("ERROR. Lista vacia o inexistente.")

    return datos_modificados

def obtener_dato(diccionario:dict,clave:str)->bool:
    """
    Brief:
    Verifica si el diccionario no se encuentra vacio,de ser asi obtiene el valor del dato pasado por parametro.

    Parametro/s:
    Recibe el diccionario en el cual trabajar y dato del valor a obtener

    Return:
    Retorna el valor del dato si fue encontrado y si no devuelve False
    
    """
    if len(diccionario)>0 and clave in diccionario:
        dato_encontrado = diccionario[clave]
    else:
        dato_encontrado = False

    return dato_encontrado

def obtener_nombre(diccionario:dict):
    """
    Brief:
    Verifica si el diccionario esta vacio,de no ser asi, obtiene el valor de la key  "nombre" y lo utiliza en un string.

    Parametro/s:
    Recibe el diccionario en el cual trabajar

    Return:
    Si la key "nombre" existe en el diccionario devuelve un string con el valor, y si no, devuelve False
    """
    if len(diccionario)>0:
        nombre = obtener_dato(diccionario,"nombre")
        mostrar_nombre = f"Nombre: {nombre}"

    else:
        mostrar_nombre = False

    return mostrar_nombre

def obtener_nombre_y_dato(diccionario:dict,clave:str):
    """
    Brief:
    Verifica si el diccionario esta vacio,de no ser asi, obtiene el valor de la key "nombre" y el valor de la key recibida en su llamada y los utiliza en un string

    Parametro/s:
    Recibe el diccionario en el cual trabajar y la key de la cual se precisa el valor.

    Return:
    Devuelve un string con el valor de la key nombre y con la del dato que recibe en su llamada.
    
    """
    if len(diccionario)>0:
        valor = diccionario[clave]
        nombre = obtener_nombre(diccionario)
        mostrar_dato = f"{nombre} | {clave}: {valor}"
    else:
        mostrar_dato = False

    return mostrar_dato

def obtener_maximo(lista:list,clave:str):
    """
    Brief:
    Verifica si el diccionario esta vacio,de no ser asi, si el dato que recibe en su llamada es de tipo Float o Int recorre la lista buscando el valor mas alto que encuentre

    Parametro/s:
    Recibe la lista a recorrer y la key de la cual quiere obtener el valor.

    Return:
    Devuelve el valor maximo de la key,siempre y cuando, la key cumple con que sea de tipo Int o Float,de no ser asi,devuelve False.
    """
    valor_maximo = 0

    if len(lista)>0:
        for diccionario in lista:
            if clave in diccionario:
                valor = obtener_dato(diccionario,clave)
                if type(valor) == float or type(valor) == int:
                    if valor > valor_maximo:
                        valor_maximo = valor
                else:
                    valor_maximo = False
    else:
        valor_maximo = False

    return valor_maximo

def obtener_minimo(lista:list,clave:str):
    """
    Brief:
    Verifica si el diccionario esta vacio,de no ser asi, si el dato que recibe en su llamada es de tipo Float o Int recorre la lista buscando el valor mas bajo que encuentre.

    Parametro/s:
    Recibe la lista a recorrer y la key de la cual quiere obtener el valor.

    Return:
    Devuelve el valor maximo de la key,siempre y cuando, la key cumple con que sea de tipo Int o Float,de no ser asi,devuelve False.
    """
    valor_minimo = float('inf')

    if len(lista)>0:
        for diccionario in lista:
            if clave in diccionario:
                valor = obtener_dato(diccionario,clave)
                if type(valor) == float or type(valor) == int:
                    if valor < valor_minimo:
                        valor_minimo = valor
                else:
                    valor_minimo = False
    else:
        valor_minimo = False

    return valor_minimo

def obtener_dato_cantidad(lista:list,filtro:str,clave:str):
    """
    Brief:
    Busca los valores maximos y altos(dependiendo lo que ingreso el usuario) del valor de la key que recibe en su llamada 

    Parametro/s:
    Recibe la lista a recorrer y la key de la cual quiere obtener el valor y el extremo por el cual desea filtrar(maximo o minimo).

    Return:
    Devuelve una lista con los nombres de los heroes que cumplan con un extremo u otro.
    """
    lista_heroes_altura = []
    if filtro == "maximo":
        maximo = obtener_maximo(lista,clave)
        for heroe in lista:
            if heroe[clave] == maximo:
                nombre_mayor = obtener_nombre(heroe)
                lista_heroes_altura.append(nombre_mayor)
        

    elif filtro == "minimo":
        minimo = obtener_minimo(lista,clave)
        for heroe in lista:
            if heroe[clave] == minimo:
                nombre_menor = obtener_nombre(heroe)
                lista_heroes_altura.append(nombre_menor)

    return lista_heroes_altura

def stark_imprimir_heroes(lista:list):
    """
    Brief:
    Recorre la lista e imprime en pantalla todos los datos de los heroes

    Parametro/s:
    Recibe la lista a recorrer.

    Return:
    Devuelve False en caso de que la lista este vacia.
    """
    if len(lista)>0:
        for heroe in lista:
            print(heroe)
    else:
        return False


def sumar_dato_heroe(lista:list,clave:str):
    """
    Brief:
    Si la key que recibe en su llamada es de tipo Int o Float acumula los valores de todos los personajes que posean esta key.

    Parametro/s:
    Recibe la lista a recorrer y la key de la cual quiere obtener el valor.

    Return:
    Devuelve el valor total acumulado de la key y si la key no es de tipo Int o Float devuelve False.
    """
    acumular_valor = 0
    for diccionario in lista:
        if type(diccionario) == dict and len(diccionario)>0:
            if clave in diccionario:
                valor = obtener_dato(diccionario,clave)
                acumular_valor += valor

        else:
            return False

    return acumular_valor

def dividir(dividendo:int,divisor:int):
    """
    Brief:
    Divide un numero por otro y devuelve el resultado

    Parametro/s:
    Recibe un numero y el numero por el cual quiere ser dividido

    Return:
    Devuelve el resultado de la operacion y en caso de que el divisor sea = 0, devuelve False.
    """
    if divisor == 0:
        return False
    else:
        resultado = dividendo / divisor
        return resultado

def calcular_promedio(lista:list,clave:str):
    """
    Brief:
    Verifica el promedio del valor de la key que recibe en su llamada 
    Parametro/s:
    Recibe la lista a recorrer y la key de la cual quiere realizar el promedio

    Return:
    Devuelve el resultado de la operacion.
    """
    contador_heroe = 0
    valor = sumar_dato_heroe(lista,clave)

    for diccionario in lista:
        if clave in diccionario:
            contador_heroe += 1

    promedio = dividir(valor,contador_heroe)
    return promedio 

def mostrar_promedio_dato(lista:list,clave:str):
    """
    Brief:
    Imprime en pantalla el valor de la operacion realizada en la funcion anterior.

    Parametro/s:
    Recibe la lista a recorrer y la key de la cual quiere realizar el promedio.

    Return:
    Devuelve un string del promedio del valor de la key,y en caso de no ser un Int o Float,devuelve False
    """
    if len(lista)>0:
        valor_promedio = calcular_promedio(lista,clave)
        if type(valor_promedio) != int and type(valor_promedio) != float:
            return False
        else:
            print(f"{valor_promedio:.2f}")
    else:
        return False

def imprimir_heroes_nb(lista:list):
    """
    Brief:
    Imprime por consola una lista con los nombres de todos los heroes cuyo genero sea NB

    Parametro/s:
    Recibe la lista a recorrer.

    Return:
    Nada
    """
    lista_genero_nb = []
    for heroe in lista:
        genero = obtener_dato(heroe,"genero")
        if genero == "NB":
            nombre = obtener_nombre(heroe)
            lista_genero_nb.append(nombre)

    print("Lista de heroes del genero NB\n------------------------------")
    stark_imprimir_heroes(lista_genero_nb)


def obtener_heroe_max_min(lista:list,clave:str,genero:str,filtro:str): 
    """
    Brief:
    Imprime por pantalla una lista con los maximos o minimos del valor de la key que recibe en su llamada segun el genero del heroe.

    Parametro/s:
    Recibe la lista a recorrer y la key de la cual quiere obtener el valor ,el genero por el cual desea buscar, y el filtro de maximo o minimo

    Return:
    Nada
    """
    lista_personajes_max_min = []
    for heroe in lista:
        if heroe["genero"] == genero:
            lista_personajes_max_min.append(heroe)

    if len(lista_personajes_max_min)>0:
        valor_min_max = obtener_dato_cantidad(lista_personajes_max_min,filtro,clave)         
        stark_imprimir_heroes(valor_min_max)

def obtener_fuerza_promedio_nb(lista:list):
    """
    Brief:
    Imprime por pantalla la fuerza promedio de los heroes que su genero sea "NB"

    Parametro/s:
    Recibe la lista a recorrer.

    Return:
    Nada
    """
    lista_personajes_nb = []
    for heroe in lista:
        if heroe["genero"] == "NB":
            lista_personajes_nb.append(heroe)

    mostrar_promedio_dato(lista_personajes_nb, "fuerza") 

def mostrar_diccionarios(diccionario:dict):
    """
    Brief:
    Normaliza los datos de un diccionario y los utiliza en un string.

    Parametro/s:
    Recibe el diccionario del cual recibe los datos.

    Return:
    Nada
    """
    for clave,valor in diccionario.items():
        print(f"{clave}: {valor}")

def contar_heroe_segun_atributo(lista:list,atributo:str):
    """
    Brief:
    Crea un diccionario en el cual cuenta la cantidad de heroes que compartan un mismo atributo

    Parametro/s:
    Recibe la lista a recorrer y el atributo por el cual se quiere realizar el conteo.

    Return:
    Devuelve un diccionario cuya clave es el valor del atributo y su valor es la cantidad de heroes que la posean.
    """
    contar = {}
    for heroe in lista:
        if atributo in heroe:
            valor = obtener_dato(heroe,atributo)
            if valor in contar:
                contar[valor] +=1
            else:
                contar[valor] = 1

    mostrar_diccionarios(contar)

def listar_heroe_segun_atributo(lista:list,atributo:str):    
    """
    Brief:
    Crea un diccionario en el cual muestra los nombre de los heroes que compartan un mismo atributo

    Parametro/s:
    Recibe la lista a recorrer y el atributo por el cual se lista.

    Return:
    Devuelve un diccionario cuya clave es el valor del atributo y su valor es el nombre de los heroes que lo posean.
    """
    contar = {}
    for heroe in lista:
        if atributo in heroe:
            valor = obtener_dato(heroe,atributo)
            if len(valor)== 0:
                valor = "No tiene"
            valor_nombre = obtener_dato(heroe,"nombre")
            if valor in contar:
                contar[valor] += f" {valor_nombre}"
            else:
                contar[valor] = f"{valor_nombre}"

    mostrar_diccionarios(contar)

menu = ["--------------------------------------------------------------------------------------\n\t\t\t\t MENU PRINCIPAL\n--------------------------------------------------------------------------------------",
        "1. Normalizar datos (No se debe poder acceder a los otros puntos)","2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB",
        "3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F","4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M",
        "5. Recorrer la lista y determinar cuál es el superhéroe más débil de género M","\n6. Siguiente pagina","7. Salir"]


sub_menu = ["--------------------------------------------------------------------------------------\n\t\t\t\t   SUB-MENU\n--------------------------------------------------------------------------------------",
            "1. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB","2. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB",
            "3. Determinar cuántos superhéroes tienen cada tipo de color de ojos.","4. Determinar cuántos superhéroes tienen cada tipo de color de pelo.",
            "5. Listar todos los superhéroes agrupados por color de ojos.","6. Listar todos los superhéroes agrupados por tipo de inteligencia",
            "\n\n7. Pagina anterior"]

def imprimir_menu(menu:list):
    """
    Brief:
    Imprime cada una de las opciones de un menu.

    Parametro/s:
    Recibe el menu con sus opciones.

    Return:
    Nada
    """
    for opcion in menu:
        print(opcion)

def validar_entero(numero:str):
    """
    Brief:
    Valida si el numero ingresado es entero.

    Parametro/s:
    Recibe el numero el cual valida.

    Return:
    Devuelve True si es un digito y False en caso de no serlo
    """
    return numero.isdigit()

def stark_menu_principal(lista:list):
    """
    Brief:
    Imprime en pantalla el menu con las opciones y le pide al usuario que ingrese un numero que sera verificado por la funcion anterior 

    Parametro/s:
    Recibe el menu del cual va a imprimir sus opciones

    Return:
    Si el usuario ingreso un digito,devuelve su valor,si no, devuelve False
    """
    imprimir_menu(lista)
    respuesta = (input("\nIngrese una opcion: "))
    if validar_entero(respuesta):
        return int(respuesta)
    else:
        return False


def star_marvel_app_sub(lista:list):
    """
    Brief:
    Crea un sub menu stark el cual dependiendo la opcion que ingreso el usuario,llama a la funcion que le corresponda.

    Parametro/s:
    Recibe la lista de la cual va a imprimir sus opciones

    Return:
    Nada
    """
    seguir = True 
    while seguir:
        respuesta = stark_menu_principal(lista)
        match respuesta:
            case 1:
                obtener_heroe_max_min(lista_personajes,"fuerza","NB","minimo")
            case 2:
                obtener_fuerza_promedio_nb(lista_personajes)
            case 3:
                contar_heroe_segun_atributo(lista_personajes,"color_ojos")
            case 4:
                contar_heroe_segun_atributo(lista_personajes,"color_pelo")
            case 5:
                listar_heroe_segun_atributo(lista_personajes,"color_ojos")
            case 6:
                listar_heroe_segun_atributo(lista_personajes,"inteligencia")
            case 7:
                seguir = False

def stark_marvel_app(lista:list):
    """
    Brief:
    Crea un menu de stark el cual dependendiendo la opcion que ingreso el usuario,llama a la funcion que corresponda,en caso de que la opcion 1 "Normalizar datos" no haya sido 
    seleccionada no se podra ingresar a las demas.

    Parametro/s:
    Recibe la lista de la cual va a imprimir sus opciones

    Return:
    Nada
    """
    datos_normalizados = False
    seguir = True 
    while seguir:
        respuesta = stark_menu_principal(lista)
        if not datos_normalizados and respuesta >1:
            print("ERROR. Primero se deben normalizar los datos con el punto 1.")
            break
        match respuesta:
            case 1:
                stark_normalizar_datos(lista_personajes)
                datos_normalizados = True
            case 2:
                imprimir_heroes_nb(lista_personajes)              
            case 3:
                obtener_heroe_max_min(lista_personajes,"altura","F","maximo")
            case 4:
                obtener_heroe_max_min(lista_personajes,"altura","M","maximo")
            case 5:
                obtener_heroe_max_min(lista_personajes,"fuerza","M","minimo")
            case 6:
                star_marvel_app_sub(sub_menu)

            case 7:
                seguir = False





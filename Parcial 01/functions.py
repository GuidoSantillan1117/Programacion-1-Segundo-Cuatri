import pygame
from datos import lista
from constantes import *

def crear_sub_listas(lista:list,clave:str):
    """"
    Brief:
    Recorre la lista de diccionario con los datos y los guarda en sub-listas

    Parametro/s:
    Recibe la lista la cual recorrer y la clave del valor a obtener.

    Return:
    Devuelve una sublista.

    """
    sub_lista = []
    for nivel in lista:
        sub_lista.append(nivel[clave])
    return sub_lista

def crear_sub_listas_diccionarios(lista:list,clave:str):
    """
    Brief:
    Recorre la lista de diccionario con los datos y los guarda en sub-listas con diccionarios:

    Parametro/s:
    Recibe la lista la cual recorrer y la clave del valor a obtener.

    Return:
    Devuelve una sublista de diccionarios.
    """
    sub_lista_diccionarios = []
    for nivel in lista:
        sub_lista_diccionarios.append({clave:nivel[clave]})

    return sub_lista_diccionarios

lista_preguntas = crear_sub_listas(lista,"pregunta")
lista_correctas = crear_sub_listas(lista,"correcta")
lista_opcion_a = crear_sub_listas_diccionarios(lista,"a")
lista_opcion_b = crear_sub_listas_diccionarios(lista,"b")
lista_opcion_c = crear_sub_listas_diccionarios(lista,"c")

def obtener_valor(lista:list,indice:int,clave:str):
    """
    Brief:
    Obtiene el valor de una clave en una determinada posicion de la lista.

    Parametro/s:
    Recibe la lista,la posicion en la lista y el valor que quiere buscar

    Return:
    Retorna el valor de la clave
    """
    valor = lista[indice][clave]
    return valor


def dibujar_rectangulo(pantalla:pygame.surface,color:str,x:int,y:int,ancho:int,alto:int):
    """
    Brief:
    Dibuja un rectangulo en la pantalla en una posicion determinada.

    Parametro/s:
    Recibe la superficie en la cual dibujar,el color,la posicion en X y en Y ,ancho y largo del rectangulo.

    Return:
    Nada
    """
    pygame.draw.rect(pantalla,color,(x,y,ancho,alto))

def blitear_pantalla(pantalla,superficie,x,y):
    """
    Brief:
    Actualiza la pantalla con la superficie agregada.

    Parametro/s:
    Recibe la pantalla en donde va actualizar,la superficie que agrega y su posicion en X e Y.

    Return:
    Nada
    """
    pantalla.blit(superficie,(x,y))




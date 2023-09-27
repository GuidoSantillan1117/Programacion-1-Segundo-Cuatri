import pygame
import pygame.mixer
from datos import lista
from constantes import *
from functions import *

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Pantalla
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Preguntados")

#Textos
fuente = pygame.font.Font(None,36)
fuente_respuestas = pygame.font.Font(None,250)
lista_textos = ["PREGUNTA","REINICIAR"]

#Imagenes
fondo = pygame.image.load("Parcial 01/imagenes/fondo.jpg")
imagen_preguntados = pygame.image.load("Parcial 01/imagenes/icono_river.png")

#Reescalar las imagenes
reescalar_fondo = pygame.transform.scale(fondo,(1280,960))
reescalar_imagen = pygame.transform.scale(imagen_preguntados,(360,360))

#Icono
pygame.display.set_icon(imagen_preguntados)

#Sonidos
sonido_correcto = pygame.mixer.Sound("Parcial 01/sonidos/grito_gol.wav")
sonido_correcto.set_volume(0.2)
sonido_incorrecto = pygame.mixer.Sound("Parcial 01/sonidos/sonido_silbido.mp3")
sonido_incorrecto.set_volume(0.2)

#Variables
boton_pregunta_presionado = False
respuesta = ""
contador = 0
score = 0
contador_incorrecto = 0
siguiente_pregunta = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] >=50 and event.pos[0]<= 300 and event.pos[1]>550 and event.pos[1]<650:
                respuesta = "a"
            elif event.pos[0] >=500 and event.pos[0]<= 750 and event.pos[1]>550 and event.pos[1]<650:
                respuesta = "b"
            elif event.pos[0] >=980 and event.pos[0]<= 1230 and event.pos[1]>550 and event.pos[1]<650:
                respuesta = "c"
            elif event.pos[0] >=500 and event.pos[0]<= 775 and event.pos[1]>90 and event.pos[1]<190:   
                boton_pregunta_presionado = True
                if  siguiente_pregunta == True:
                    contador +=1
                    siguiente_pregunta = False
            elif event.pos[0] >=500 and event.pos[0]<= 775 and event.pos[1]>750 and event.pos[1]<850:
                contador = 0
                score = 0

    if contador <16:
        if respuesta == lista_correctas[contador]:
            score += 10
            respuesta = ""
            siguiente_pregunta = True
            boton_pregunta_presionado = False
            sonido_correcto.play()
            if contador_incorrecto == 1:
                contador_incorrecto = 0
                contador +=1    
        elif respuesta != "" and respuesta != lista_correctas[contador]:
            respuesta = ""
            contador_incorrecto += 1
            if contador_incorrecto == 2:
                sonido_incorrecto.play()
                contador_incorrecto = 0
                boton_pregunta_presionado = False
                siguiente_pregunta = True
    else:
        contador = 0
        score = 0
    #FONDO E ICONO DEL JUEGO
    blitear_pantalla(screen,reescalar_fondo,0,0)
    blitear_pantalla(screen,reescalar_imagen,40,10)
    
    #RECTANGULOS PREGUNTAR | REINICIAR
    dibujar_rectangulo(screen,COLOR_GRIS,500,90,275,100)
    dibujar_rectangulo(screen,COLOR_GRIS,500,750,275,100)
    
    #STRING SCORE
    string_score = f"SCORE:{score}"
    draw_texto_score = fuente.render(string_score,True,COLOR_NEGRO)

    #STRING PREGUNTAR
    draw_texto = fuente.render(lista_textos[0],True,COLOR_NEGRO)
    centrar_texto_x = 500 + 275 // 2 - draw_texto.get_width() // 2
    centrar_texto_y = 90 + 100 // 2 - draw_texto.get_height() // 2

    #STRING REINICIAR
    draw_texto_reiniciar = fuente.render(lista_textos[1],True,COLOR_NEGRO)
    centrar_texto_dos_x = 500 + 275 // 2 - draw_texto_reiniciar.get_width() // 2
    centrar_texto_dos_y = 750 + 100 // 2 - draw_texto_reiniciar.get_height() // 2

    #BLITEAR LOS TEXTOS
    blitear_pantalla(screen,draw_texto,centrar_texto_x,centrar_texto_y)
    blitear_pantalla(screen,draw_texto_reiniciar,centrar_texto_dos_x,centrar_texto_dos_y)
    blitear_pantalla(screen,draw_texto_score,1100,20)

    if  boton_pregunta_presionado:
        draw_texto_preguntas = fuente.render(lista_preguntas[contador],True,COLOR_NEGRO)
        valor_a = obtener_valor(lista,contador,"a")
        valor_b = obtener_valor(lista,contador,"b")
        valor_c = obtener_valor(lista,contador,"c")

        draw_texto_respuestas_a = fuente.render(valor_a, True, COLOR_BLANCO)
        draw_texto_respuestas_b = fuente.render(valor_b, True, COLOR_BLANCO)
        draw_texto_respuestas_c = fuente.render(valor_c, True, COLOR_BLANCO)

        centrar_opcion_a_x = 50 +250 // 2 - draw_texto_respuestas_a.get_width() // 2
        centrar_opcion_a_y= 550 + 100 // 2 - draw_texto_respuestas_a.get_height() //2


        centrar_opcion_b_x = 500 +250 // 2 - draw_texto_respuestas_b.get_width() // 2
        centrar_opcion_b_y= 550 + 100 // 2 - draw_texto_respuestas_b.get_height() //2

        centrar_opcion_c_x = 980 +250 // 2 - draw_texto_respuestas_c.get_width() // 2
        centrar_opcion_c_y= 550 + 100 // 2 - draw_texto_respuestas_c.get_height() //2
        
        #RECTANGULOS OPCIONES
        dibujar_rectangulo(screen,COLOR_ROJO,50,550,250,100)
        dibujar_rectangulo(screen,COLOR_ROJO,500,550,250,100)
        dibujar_rectangulo(screen,COLOR_ROJO,980,550,250,100)

        #PREGUNTAS Y OPCIONES
        blitear_pantalla(screen,draw_texto_preguntas,40,400)
        blitear_pantalla(screen,draw_texto_respuestas_a,centrar_opcion_a_x,centrar_opcion_a_y)
        blitear_pantalla(screen,draw_texto_respuestas_b,centrar_opcion_b_x,centrar_opcion_b_y)
        blitear_pantalla(screen,draw_texto_respuestas_c,centrar_opcion_c_x,centrar_opcion_c_y)
        
    pygame.display.update()
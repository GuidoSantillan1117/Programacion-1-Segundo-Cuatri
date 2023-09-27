# Ejercicio 1

# pedir_nombre = input("Ingrese su nombre: ")
# pedir_sueldo = float(input("Ingrese su sueldo: "))

# sueldo_incrementado = pedir_sueldo * 1.10

# print(f"Nombre: {pedir_nombre} | Sueldo: {sueldo_incrementado}")

# Ejercicio 2

# pedir_edad = int(input("Ingrese su edad:"))
# if pedir_edad > 17:
#     edad = "Mayor de edad."
# else:
#     if pedir_edad >12 and pedir_edad<18:
#         edad = "Mayor de 13 años."
#     else:
#         edad = "Menor de 13 años."

# print(edad)

# Ejercicio 3

# contador_pares = 0
# contador_impares = 0

# sumar_positivos = 0
# multiplicar_negativos = 1

# numero_menor = 0
# mayor_par_ingresado = 0

# for i in range(5):
#     pedir_numero = int(input("Ingrese un numero:"))
#     while pedir_numero == 0:
#         pedir_numero = int(input("Ingrese un numero:"))

#     if pedir_numero % 2 == 0:
#         contador_pares += 1
#         if pedir_numero > mayor_par_ingresado:
#             mayor_par_ingresado = pedir_numero
#     else:
#         contador_impares +=1

#     if pedir_numero < numero_menor:
#         numero_menor = pedir_numero

#     if pedir_numero > 0:
#         sumar_positivos += pedir_numero
#     elif pedir_numero <0:
#         multiplicar_negativos *= pedir_numero

# print(f"a. Cantidad de pares: {contador_pares} | Impares: {contador_impares}")
# print(f"b. El menor número ingresado: {numero_menor}")
# print(f"c. De los pares el mayor número ingresado: {mayor_par_ingresado}")
# print(f"d. Suma de los positivos: {sumar_positivos}")
# print(f"e. Producto de los negativos: {multiplicar_negativos}")

# Ejercicio 4

# pedir_edad = int(input("Ingrese su edad: "))
# pedir_estado_civil = input("Ingrese su estado civil: ")

# if pedir_edad <18 and pedir_estado_civil != "Soltero":
#     print("Es muy pequeño para NO ser soltero")

# Ejercicio 5

# estadia_base = 15000
# ingresar_estacion = input("Ingrese una estacion del año:")
# ingresar_localidad = input("Ingrese una localidad:")

# estaciones = ["Verano","Invierno","Otoño","Primavera"]
# localidades = ["Bariloche","Cataratas","Mar del Plata","Cordoba"]

# if ingresar_estacion not in estaciones or ingresar_localidad not in localidades:
#     print("Estacion o localidad invalida.")
# else:
#     if ingresar_estacion == "Invierno":
#         if ingresar_localidad == "Bariloche":
#             precio_final = estadia_base * 1.20
#         elif ingresar_localidad == "Cataratas" or ingresar_localidad == "Cordoba":
#             precio_final = estadia_base * 0.90
#         elif ingresar_localidad == "Mar del Plata":
#             precio_final = estadia_base *0.80

#     elif ingresar_estacion == "Verano":
#         if ingresar_localidad == "Bariloche":
#             precio_final = estadia_base * 0.80
#         elif ingresar_localidad == "Cataratas" or ingresar_localidad == "Cordoba":
#             precio_final = estadia_base * 1.10
#         elif ingresar_localidad == "Mar del Plata":
#             precio_final = estadia_base *1.20

#     elif ingresar_estacion == "Otoño" or ingresar_estacion == "Primavera":
#         if ingresar_localidad == "Bariloche":
#             precio_final = estadia_base * 1.10
#         elif ingresar_localidad == "Cataratas":
#             precio_final = estadia_base * 1.10
#         elif ingresar_localidad == "Mar del Plata":
#             precio_final = estadia_base * 1.10
#         elif ingresar_localidad == "Cataratas":
#             precio_final = estadia_base * 1

#     print(f"Estacion ingresada: {ingresar_estacion} | Localidad ingresada: {ingresar_localidad} | Precio final = {precio_final}")
        

#EJERCICIO 6

lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

mayor_numero = 0

for i in lista_numeros:
    if i > mayor_numero:
        mayor_numero = i

print(mayor_numero)

#EJERCICIO 7 

lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

for i in lista_numeros:
    if i % 2 == 0:
        print(i)

#EJERCICIO 8

lista_numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]

lista_sin_repetir = []

for i in lista_numeros:
    if i not in lista_sin_repetir:
        lista_sin_repetir.append(i)
    else:
        print(i)

#EJERCICIO 9

edades = [25,36,18,23,45]

nombre = ["Juan","Ana","Sol","Mario","Sonia"]

menor_numero = 100

for i in edades:
    if i < menor_numero:
        menor_numero = i

posicion = edades.index(menor_numero)
nombre_mas_joven = nombre[posicion]

print(f"La persona mas joven es: {nombre_mas_joven} con {menor_numero} años.")

#EJERCICIO 10

lista_nombres = []
lista_genero = []
lista_notas = []

nota_mas_baja = 10
sumar_notas = 0
contador_mujeres = 0

nombre_hombre = None

for i in range(5):
    ingresar_nombre = input("Ingresar nombre: ")
    ingresar_genero = input("Ingresar genero: F o M")
    while ingresar_genero != "F" and ingresar_genero != "M":
        ingresar_genero = input("Genero invalido,reingresar genero: F o M")

    ingresar_nota = int(input("Ingresar nota: "))
    while ingresar_nota < 0 or ingresar_nota >10:
        ingresar_nota = int(input("Nota invalida,reingresar nota: "))

    lista_nombres.append(ingresar_nombre)
    lista_genero.append(ingresar_genero)
    lista_notas.append(ingresar_nota)

    if ingresar_genero == "M" and ingresar_nota < nota_mas_baja:
        nota_mas_baja = ingresar_nota
        nombre_hombre = ingresar_nombre

    if ingresar_genero == "F":
        contador_mujeres += 1
        sumar_notas += ingresar_nota

if contador_mujeres > 0:
    promedio_notas = sumar_notas / contador_mujeres 
else:
    promedio_notas = "No se puede realizar un promedio ya que no se ingreso ningun genero femenino."

print(f"Nombre del hombre con nota más baja: {nombre_hombre}")
print(f"Promedio de notas de las mujeres: {promedio_notas}")
print(f"Lista de datos ingresados\nNombre: {lista_nombres}\nGenero: {lista_genero} \nNota: {lista_notas}")
    



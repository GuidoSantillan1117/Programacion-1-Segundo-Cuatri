##Integrador 001 Guido Santillan DIV J

maximo_precio = 0
acumular_unidades_jabon = 0
cantidad_unidades_max = 0

for i in range(2):
    tipo_producto = input("Ingrese el tipo del producto: ")
    tipo_productos_validos = ["Barbijo","Jabon","Alcohol"]
    while tipo_producto not in tipo_productos_validos:
        tipo_producto = input("Reingrese un tipo de producto valido: ")

    precio_producto = float(input("Ingrese el precio del producto: "))
    while precio_producto <100 or precio_producto > 300:
        precio_producto = float(input("Reingrese el precio del producto (Entre $100 y $300: ) "))
    cantidad_unidades = int(input("Ingrese la cantidad de unidades del producto: "))
    while cantidad_unidades < 1 or cantidad_unidades >1000:
        cantidad_unidades = int(input("Reingrese la cantidad de unidades (Entre 1 y 1000): "))
    marca_producto = input("Ingrese la marca del producto: ")
    fabricante_producto = input("Ingrese el fabricante del producto: ")

    match (tipo_producto):
        case "Barbijo":
            if precio_producto > maximo_precio:
                maximo_precio = precio_producto
                cantidad_mas_caro = cantidad_unidades
                fabricante_mas_caro = fabricante_producto
        case "Jabon":
            acumular_unidades_jabon += cantidad_unidades

    if cantidad_unidades > cantidad_unidades_max:
        cantidad_unidades_max = cantidad_unidades
        item_max_unidades = tipo_producto
        fabricante_max_unidades = fabricante_producto

print(f"---------------------------------------------------------------------------")
print(f"Del más caro de los barbijos: (${maximo_precio}) , la cantidad de unidades: {cantidad_mas_caro} y el fabricante: {fabricante_mas_caro}")
print(f"Del ítem con más unidades: {item_max_unidades} , el fabricante: {fabricante_max_unidades}")
print(f"Cuántas unidades de jabones hay en total: {acumular_unidades_jabon}")

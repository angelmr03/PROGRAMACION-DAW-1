
# Lista de opciones disponibles
opciones = ["cuadrado", "rectangulo", "salir"]

# La funcion para que luego simplemente se ponga abajo y no hacerlo 1 a 1
def calcular_area_perimetro_cuadrado(lado):
    
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro

# En la del rectangulo hay que añadir base y altura
def calcular_area_perimetro_rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

# Para dibujar el cuadrado, pintara los asteriscos que pongas
# Si el lado es 3, pintara 3 asteriscos en una linea, y el mismo numero de lineas
def dibujar_cuadrado(lado):
    for _ in range(lado):
        print("* " * lado)

# Para dibujar el rectangulo
def dibujar_rectangulo(base, altura):
    """Dibuja un rectángulo con asteriscos"""
    for _ in range(altura):
        print("* " * base)

# Bucle infinito y se rompe cuando sea válida la opción
# Esta es la estructura con la que ya sacamos las cosas
while True:
    figura = input("Elige cuadrado, rectángulo o salir: ").lower()

    # Cuando sea cuadrado:
    if figura == "cuadrado":
        lado_cuadrado = int(input("Ingrese la longitud de los lados: "))
        area, perimetro = calcular_area_perimetro_cuadrado(lado_cuadrado)
        print(f"El área del cuadrado es {area}")
        print(f"El perímetro del cuadrado es {perimetro}")
        print("La figura del cuadrado:")
        #La funcion con la que dibujamos el cuadrado
        dibujar_cuadrado(lado_cuadrado)

    # Cuando sea rectangulo:
    elif figura == "rectangulo":
        base_rectangulo = int(input("Ingrese la longitud de la base: "))  # Base del rectángulo
        altura_rectangulo = int(input("Ingrese la altura del rectángulo: "))  # Altura del rectángulo
        area, perimetro = calcular_area_perimetro_rectangulo(base_rectangulo, altura_rectangulo)
        print(f"El área del rectángulo es {area}")
        print(f"El perímetro del rectángulo es {perimetro}")
        print("Aquí está tu rectángulo:")
        #La funcion con la que dibujamos el rectángulo
        dibujar_rectangulo(base_rectangulo, altura_rectangulo)

    # Cuando sea salir ( y se rompe el bucle ):
    elif figura == "salir":
        break
    
    # Cuando no sea ninguna de las anteriores dara error:
    else:
        print("Error, opción no válida. Vuelve a intentarlo.")

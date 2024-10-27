# Hay que importar el modulo random para poder seleccionar luego aleatoriamente la opcion del ordenador 
import random 

opciones = ["tijera", "papel", "piedra"]

# Para llevar la cuenta de las victorias
victorias_usuario = 0
victorias_ordenador = 0

# Con este bucle se repetira hasta que uno gane 3 veces
while victorias_usuario < 3 and victorias_ordenador < 3:
    
    # Se elige
    usuario = input("Elige piedra, papel o tijera:").lower()
    ordenador = random.choice(opciones)

    # Si hay error te vuelve a pedir elegir
    if usuario not in opciones:
        print("Error")
        continue

    # Si las opciones son iguales, empate
    if usuario == ordenador:
        print(f"El ordenador eligio {ordenador}")
        print("Empate")
        print(f"Marcador -> Usuario: {victorias_usuario}, Ordenador: {victorias_ordenador}")
    
    # Las opciones para que gane el ordenador
    elif usuario == "tijera" and ordenador == "piedra" \
        or usuario == "piedra" and ordenador == "papel" \
            or usuario == "papel" and ordenador == "tijera": 
        victorias_ordenador += 1
        print(f"El ordenador eligio {ordenador}")
        print("Has perdido")
        print(f"Marcador -> Usuario: {victorias_usuario}, Ordenador: {victorias_ordenador}")
    
    # Las opciones para que gane el usuario 
    else:
        victorias_usuario += 1
        print(f"El ordenador eligió {ordenador}")
        print("Has ganado")
        print(f"Marcador -> Usuario: {victorias_usuario}, Ordenador: {victorias_ordenador}")
    
# Si gana el usuario:
if victorias_usuario == 3:
    print("Ha ganado el juego")

# Si gana el ordenador:
else:
    print("Ha perdido el juego")





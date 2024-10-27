# La función que nos permite depositar dinero en la cuenta
def depositar(saldo, cantidad):
    saldo += cantidad
    return saldo

# La función que nos permite sacar dinero de la cuenta
def sacar(saldo, cantidad):
    saldo -= cantidad
    return saldo

# Inicializamos las estadísticas de dinero ingresado y retirado
total_ingresado = 0
total_retirado = 0

# Bucle para iniciar el saldo, tiene que ser mayor que 0 
while True:
    saldo = float(input("Ingrese el saldo inicial: "))
    if saldo >= 0:
        break
    else:
        print("El saldo no puede ser negativo. Intente de nuevo.")

# Bucle principal para realizar todas las operaciones 
while True:
    opcion = input("\nBienvenido a la cuenta bancaria.\n1 - Ingresar dinero\n 2 - Retirar dinero\n3 - Mostrar saldo\n4 - Estadísticas\n5 - Salir\nElija una opción: ").strip()
    
    # Para salir
    if opcion == "5":
        print("Gracias por usar el sistema bancario. ¡Hasta luego!")
        break
    # Para ingresar dinero
    elif opcion == "1":
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        if cantidad > 0:
            saldo = depositar(saldo, cantidad)
            total_ingresado += cantidad
            print(f"El saldo después del depósito es {saldo} €")
        else:
            print("No se puede depositar una cantidad negativa o cero.")
    # Para retirar dinero
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if cantidad > 0:
            if saldo >= cantidad:
                saldo = sacar(saldo, cantidad)
                total_retirado += cantidad
                print(f"El saldo después de la retirada es {saldo} €")
            else:
                print("Fondos insuficientes. No puede quedarse en números rojos.")
        else:
            print("No se puede retirar una cantidad negativa o cero.")
    # Para consultar el saldo
    elif opcion == "3":
        print(f"Su saldo actual es {saldo} €")
    # Para ver las estadisticas de las operaciones
    elif opcion == "4":
        print(f"Estadísticas:\nTotal ingresado: {total_ingresado} €\nTotal retirado: {total_retirado} €")
    # Si no esta entre las opciones, repeticion del bucle
    else:
        print("Opción no válida. Intente de nuevo.")

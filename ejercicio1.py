# Defino una lista de números permitidos
permitidos= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    try:
        numero_ingresado = int(input("Por favor, ingresa un número del 0 al 9: "))
    
        # Comprobuebo si el número ingresado por el usuario está en la lista de números permitidos
        if numero_ingresado in permitidos:
            print(f"¡El número {numero_ingresado} está en la lista de números permitidos!")
            break  
        else:
            print("El número no está en la lista. Inténtalo de nuevo.")
    except ValueError:
        print("Entrada no válida. Debes ingresar un número entero del 0 al 9.")


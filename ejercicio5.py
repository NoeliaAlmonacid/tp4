try:
    resultado = 15 + "20"
except TypeError as e:
    mensaje = f"Se produjo un error: {e}. La causa podría ser que estás intentando sumar un número con una cadena. Asegúrate de que ambos operandos sean del mismo tipo."
    print(mensaje)

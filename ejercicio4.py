usuarios_info = []


def ingresar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    edad = input("Ingrese la edad del usuario: ")
    direccion = input("Ingrese la dirección del usuario: ")
    telefono = input("Ingrese el teléfono del usuario: ")

    # Diccionario con la información del usuario
    usuario = {
        "Nombre": nombre,
        "Edad": edad,
        "Dirección": direccion,
        "Teléfono": telefono
    }

    # Agregar el diccionario del usuario a la lista de usuarios_info
    usuarios_info.append(usuario)

# Se le pide al usuario que ingrese información para varios usuarios


while True:
    ingresar_usuario()
    continuar = input("¿Desea ingresar información de otro usuario? (S/N): ")
    if continuar.lower() != "s":
        break

# Mostrara la información ingresada

for indice, usuario in enumerate(usuarios_info, start=1):
    print(f"Información del Usuario {indice}:")
    for clave, valor in usuario.items():
        print(f"{clave}: {valor}")
    print()

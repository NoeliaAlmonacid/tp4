# Defino un conjunto usuarios
usuarios= {"Marcela","David","Elvira", "Juan","Marcos"}

# Defino un conjunto de administradores, luego borro a Juan.

administradores= {"Juan","Marcela"}
administradores.discard("Juan")
administradores.add("Marcos")

for usuario in usuarios:
    if usuario in administradores:
        print(f"{usuario} es Administrador.")
    else:
        print(f"{usuario} es un usuario, pero no es Administrador.")
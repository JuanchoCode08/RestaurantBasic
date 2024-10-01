#Funciones para desarrollar el login


# Diccionario de usuarios y contraseñas existentes
usuarios = {
    "admin": "1234",  # Usuario administrador
    "juan": "contraseña123"
}

# Función para iniciar sesión
def iniciar_sesion():
    print("---- Iniciar Sesión ----")
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    # Verificamos si el usuario existe y la contraseña es correcta
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
        return usuario
    else:
        print("Nombre de usuario o contraseña son incorrectos.")
        return None

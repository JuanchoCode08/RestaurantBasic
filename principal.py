#Llamando la funcion de login
from login import iniciar_sesion


# Menú inicial del restaurante
menu = {
    "Salchipapa": 9.50,
    "Hot Dogs": 6.50,
    "Pizza": 8.50,
    "Hamburguesa": 5.00,
    "Ensalada": 4.50,
    "Refresco": 1.50,
    "Tarta": 3.00
}

# Función para mostrar el menú
def mostrar_menu() :
    print("\n--- Menú del Restaurante ---")
    for plato, precio in menu.items():
        print(f"{plato}: ${precio:.2f}")
    print("----------------------------")
    
# Función para agregar un nuevo plato al menú (Funcion solo para el admin)
def agregar_plato() :
    nuevo_plato = input("Nombre del nuevo plato: ").capitalize()
    precio = float(input(f"Precio para {nuevo_plato}: $"))
    menu[nuevo_plato] = precio
    print(f"{nuevo_plato} ha sido añadido al menú con un precio de ${precio:.2f}")

# Función para eliminar un plato del menú (Funcion solo para el admin)
def eliminar_plato():
    plato_eliminar = input("Nombre del plato a eliminar: ").capitalize()
    if plato_eliminar in menu:
        del menu[plato_eliminar]
        print(f"{plato_eliminar} ha sido eliminado del menú.")
    else:
        print("El plato no está en el menú.")
        
# Función para tomar el pedido
def tomar_pedido():
    pedido = []
    total = 0
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione un plato o escriba 'fin' para terminar el pedido: ").capitalize()
        if opcion == 'Fin':
            break
        elif opcion in menu:
            cantidad = int(input(f"¿Cuántas unidades de {opcion} desea? "))
            subtotal = menu[opcion] * cantidad
            pedido.append((opcion, cantidad, subtotal))
            total += subtotal
        else:
            print("Plato no disponible, intente nuevamente.")
    
    return pedido, total

# Función para mostrar la factura
def mostrar_factura(pedido, total):
    print("\n--- Factura ---")
    for plato, cantidad, subtotal in pedido:
        print(f"{plato} x{cantidad}: ${subtotal:.2f}")
    print(f"Total a pagar: ${total:.2f}")
    print("----------------")


# Menú principal del sistema
def menu_principal() :
    usuario = iniciar_sesion()
    
    if usuario:
        while True:
            print("\n--- Bienvenido al Sistema de Restaurante de Comida Rapida ---")
            print("\nAcontinuación te mostraré las siguientes opciones disponibles")
            print("1. Mostrar Menú")
            print("2. Tomar Pedido")
            if usuario == "admin" :
                print("3. Agregar Plato al Menú")
            if usuario == "admin" :
                print("4. Eliminar Plato del Menú")
            if usuario == "admin" :
                print("5. Salir")
            else :
                print("3. Salir")
            
            opcion = input("Por favor seleccione una opción: ")
            
            if opcion == '1':
                mostrar_menu()
            elif opcion == '2':
                pedido, total = tomar_pedido()
                mostrar_factura(pedido, total)
            elif opcion == '3' :
                agregar_plato()
            elif opcion == '4' :
                eliminar_plato()
            elif opcion == '5':
                print("Gracias por usar el sistema. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")
                
if __name__ == "__main__":
    menu_principal()
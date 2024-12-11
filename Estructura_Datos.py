"""
Inserción: append(), insert(), extend().
Borrado: remove(), pop(), del.
Actualización: Asignación directa al índice, o uso de index() para buscar un valor.
Ordenación: sort(), sorted().

* EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""
""""
# Creando una lista inicial
lista = [10, 20, 30, 40]
print(f"Esta es la lista inicial : {lista}")
#Inserción al final de la lista
lista.append(50)
print("Este es el valor Después de insertar un valor al final de la lista:", lista)

# Inserción en una posición específica
lista.insert(1, 15)  # Inserta 15 en la posición 1
print("Después de insertar un valor en un lugar especifico,  posición 1:", lista)

# Inserción de múltiples elementos
lista.extend([60, 70])
print("Después de insertar varios elementos a la lista :", lista)"""
"""
#Borrar un valor de la lista
lista = [10, 20, 30, 40]
print("Lista Original", lista)
lista.remove(20)
print("La nueva lista despues de eliminar un elemento es: ", lista)

#Actualizacion por posicion
lista = [10, 20, 30, 40]
lista[2] = 25
print("Despues de actualizar el indice 2:", lista)
#Actualizacion por valor
if 40 in lista:
    index = lista.index(40)
    lista[index] = 45
    print("Despues de actualizar el valor 40 por 45:", lista)

#Ordenamiento
lista = [20, 100, 30, 60, 50]
lista.sort()
print("Lista ordenada de forma ascendente:", lista)
lista.sort(reverse=True)
print("Lista ordenada de forma descendente:", lista)"""


""""* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.

"""
# Diccionario que almacenará los contactos
agenda = []
def mostrar_agenda():
    """Muestra todos los contactos almacenados en la agenda."""
    if not agenda:
        print("La agenda está vacía.")
    else:
        for nombre, detalles in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"  Teléfono: {detalles['telefono']}")
            print(f"  Email: {detalles['email']}")
            print("-" * 30)


def buscar_contacto():
    """Busca un contacto por nombre."""
    nombre = input("Introduce el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"Contacto encontrado: {nombre}")
        print(f"  Teléfono: {agenda[nombre]['telefono']}")
        print(f"  Email: {agenda[nombre]['email']}")
    else:
        print(f"Contacto con nombre {nombre} no encontrado.")


def insertar_contacto():
    """Inserta un nuevo contacto."""
    nombre = input("Introduce el nombre del nuevo contacto: ")
    if nombre in agenda:
        print("Este contacto ya existe. Usa la opción de actualización si deseas modificarlo.")
        return
    telefono = input("Introduce el teléfono del contacto: ")
    email = input("Introduce el email del contacto: ")

    # Agregar el nuevo contacto
    agenda[nombre] = {
        'telefono': telefono,
        'email': email
    }
    print(f"Contacto {nombre} agregado correctamente.")


def actualizar_contacto():
    """Actualiza un contacto existente."""
    nombre = input("Introduce el nombre del contacto que deseas actualizar: ")
    if nombre not in agenda:
        print(f"Contacto {nombre} no encontrado.")
        return

    telefono = input(f"Introduce el nuevo teléfono para {nombre}: ")
    email = input(f"Introduce el nuevo email para {nombre}: ")

    # Actualizar el contacto
    agenda[nombre] = {
        'telefono': telefono,
        'email': email
    }
    print(f"Contacto {nombre} actualizado correctamente.")


def eliminar_contacto():
    """Elimina un contacto por nombre."""
    nombre = input("Introduce el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado correctamente.")
    else:
        print(f"Contacto con nombre {nombre} no encontrado.")


def menu():
    #Función que muestra el menú principal y permite elegir opciones.
    while True:
        print("\n--- Agenda de Contactos ---")
        print("1. Mostrar todos los contactos")
        print("2. Buscar un contacto")
        print("3. Insertar un nuevo contacto")
        print("4. Actualizar un contacto existente")
        print("5. Eliminar un contacto")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ")

        if opcion == '1':
            mostrar_agenda()
        elif opcion == '2':
            buscar_contacto()
        elif opcion == '3':
            insertar_contacto()
        elif opcion == '4':
            actualizar_contacto()
        elif opcion == '5':
            eliminar_contacto()
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 6.")


# Ejecutar el menú
menu()

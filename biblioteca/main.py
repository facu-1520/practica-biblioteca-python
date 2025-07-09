from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca


def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n📚 Menú de la Biblioteca")
        print("1. Registrar Libro")
        print("2. Registrar Usuario")
        print("3. Realizar Préstamo")
        print("4. Ver Libros")
        print("5. Ver Usuarios")
        print("6. Ver Préstamos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            id_libro = input("ID del libro: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            biblioteca.registrar_libro(Libro(id_libro, titulo, autor))
        elif opcion == "2":
            id_usuario = input("ID del usuario: ")
            nombre = input("Nombre: ")
            biblioteca.registrar_usuario(Usuario(id_usuario, nombre))
        elif opcion == "3":
            id_libro = input("ID del libro: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.prestar_libro(id_libro, id_usuario)
        elif opcion == "4":
            biblioteca.mostrar_libros()
        elif opcion == "5":
            biblioteca.mostrar_usuarios()
        elif opcion == "6":
            biblioteca.mostrar_prestamos()
        elif opcion == "0":
            print("👋 ¡Hasta la próxima!")
            break
        else:
            print("❌ Opción no válida")


if __name__ == "__main__":
    menu()

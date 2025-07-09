from prestamo import Prestamo


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, id_libro, id_usuario):
        libro = next(
            (l for l in self.libros if l.id_libro == id_libro and l.disponible), None  # noqa: E741
        )
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if libro and usuario:
            prestamo = Prestamo(libro, usuario)
            libro.disponible = False
            self.prestamos.append(prestamo)
            print("✅ Préstamo registrado exitosamente")
        else:
            print("⚠️ Error: Libro no disponible o Usuario no encontrado")

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)

    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)

    def mostrar_prestamos(self):
        for prestamo in self.prestamos:
            print(prestamo)

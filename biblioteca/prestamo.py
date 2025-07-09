from datetime import datetime


class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()

    def __str__(self):
        return f"{self.usuario.nombre} tomó '{self.libro.titulo}' el {self.fecha_prestamo.strftime('%d/%m/%Y')}"

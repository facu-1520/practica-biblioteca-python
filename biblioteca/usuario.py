class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre

    def __str__(self):
        return f"[{self.id_usuario}] {self.nombre}"

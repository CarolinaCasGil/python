class Usuario:
    def __init__(self, nombre_de_usuario):
        self.nombre_de_usuario = nombre_de_usuario
        self.publicaciones = []
        self.comentarios = []

    def crear_publicacion(self, contenido):
        publicacion = Publicacion(contenido, self)
        self.publicaciones.append(publicacion)

    def agregar_comentario(self, publicacion, contenido):
        comentario = Comentario(contenido, self)
        publicacion.agregar_comentario(comentario)
        self.comentarios.append(comentario)

class Publicacion:
    def __init__(self, contenido, usuario):
        self.contenido = contenido
        self.usuario = usuario
        self.comentarios = []

    def agregar_comentario(self, comentario):
        self.comentarios.append(comentario)

class Comentario:
    def __init__(self, contenido, usuario):
        self.contenido = contenido
        self.usuario = usuario

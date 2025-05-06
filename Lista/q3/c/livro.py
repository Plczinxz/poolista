from autor import Autor

class Livro:
    def __init__(self, titulo: str, isbn: str, autor: Autor):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        
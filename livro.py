class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def __str__(self):
        status = "disponivel" if self.disponivel else "emprestado"
        return f"{self.titulo} - {self.autor} ({status})"

from livro import Livro


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor, isbn):
        livro = Livro(titulo, autor, isbn)
        self.livros.append(livro)
        return livro

    def buscar_por_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro
        return None

    def emprestar(self, isbn):
        livro = self.buscar_por_isbn(isbn)
        if livro is None:
            print("livro nao encontrado")
            return False
        livro.disponivel = False
        return True

    def devolver(self, isbn):
        livro = self.buscar_por_isbn(isbn)
        if livro is None:
            print("livro nao encontrado")
            return False
        livro.disponivel = True
        return True

    def listar_disponiveis(self):
        disponiveis = [livro for livro in self.livros if livro.disponivel]
        if not disponiveis:
            print("nenhum livro disponivel no momento")
            return
        for livro in disponiveis:
            print(livro)

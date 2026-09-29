from biblioteca import Biblioteca

biblioteca = Biblioteca()

biblioteca.adicionar_livro("Dom Casmurro", "Machado de Assis", "111")
biblioteca.adicionar_livro("O Cortico", "Aluisio Azevedo", "222")
biblioteca.adicionar_livro("Memorias Postumas", "Machado de Assis", "333")

print("livros disponiveis:")
biblioteca.listar_disponiveis()

biblioteca.emprestar("111")
print("\napos emprestar o 111:")
biblioteca.listar_disponiveis()

print("\ntentando emprestar o 111 de novo:")
biblioteca.emprestar("111")
biblioteca.listar_disponiveis()

biblioteca.devolver("111")
print("\napos devolver o 111:")
biblioteca.listar_disponiveis()

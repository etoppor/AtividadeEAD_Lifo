#Construa agora um algoritmo para implementação de um Pilha de Livros. 
# Lembrando que na Pilha o último elemento adicionado, será o primeiro elemento removido

class Livro:
  def __init__(self, titulo, autor, paginas):
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas
    self.proximo = None

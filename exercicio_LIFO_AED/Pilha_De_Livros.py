from Livro import Livro

class PilhaDeLivros:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def empilhar(self, livro):
        novo_livro = Livro(livro['titulo'], livro['autor'], livro['paginas'])
        novo_livro.proximo = self.topo
        self.topo = novo_livro
        self.tamanho += 1
        print(f"Livro '{novo_livro.titulo}' empilhado.")

    def desempilhar(self):
        if self.topo is None:
            print("Pilha de livros está vazia.")
            return None
        livro_removido = self.topo
        self.topo = self.topo.proximo
        self.tamanho -= 1
        print(f"Livro '{livro_removido.titulo}' desempilhado.")
        return livro_removido

    def tamanho_pilha(self):
        return self.tamanho

    def listar(self):
        if self.topo is None:
            print("Pilha de livros está vazia.")
        else:
            atual = self.topo
            while atual:
                print(atual)
                atual = atual.proximo

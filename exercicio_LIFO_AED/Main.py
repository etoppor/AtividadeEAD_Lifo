from Pilha_De_Livros import PilhaDeLivros

def main():
    pilha = PilhaDeLivros()

    livro1 = {
        'titulo': "The Hunger Games",
        'autor': "Suzanne Collins",
        'paginas':400 
    }
    livro2 = {
        'titulo': "Harry Potter e a Pedra Filosofal",
        'autor': "J.K. Rowling",
        'paginas':264
    }
    livro3 = {
        'titulo': "Senhor dos Anéis",
        'autor': "J.R.R. Tolkien",
        'paginas':1184
    }

    pilha.empilhar(livro1)
    pilha.empilhar(livro2)
    pilha.empilhar(livro3)

    print(f"Tamanho da pilha: {pilha.tamanho_pilha()}")

    pilha.listar()

    livro_removido = pilha.desempilhar()
    if livro_removido:
        print(f"Livro removido: {livro_removido.titulo}")

    print(f"Tamanho da pilha: {pilha.tamanho_pilha()}")

    pilha.listar()

if __name__ == "__main__":
    main()

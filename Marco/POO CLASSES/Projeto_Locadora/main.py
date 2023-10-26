"""Projeto agenda, classe contato - nome, telefone e email*Atributos obrigatorios* e
Classe agenda - Metodo construtor que recebe uma lista de contatos vazia. *Metodo -Adicionar contato,
 lista contatos e buscar contatos, deletar contatos* 
"""
def main():
    from locadora import Locadora
    
    minha_locadora = Locadora("Minha Locadora")
    from filme import Filme
    filme1 = Filme("Matrix", "Ação", 225)
    filme2 = Filme("Vingadores", "Heroi", 110)
    filme3 = Filme("One Piece Red", "Anime", 90)

    minha_locadora.adicionar_filme(filme1)
    minha_locadora.adicionar_filme(filme2)
    minha_locadora.adicionar_filme(filme3)

    while True:
        print("\nEscolha uma opção: ")
        print("Opção 1. Listar Catálogo")
        print("Opção 2. Alugar Filme")
        print("Opção 3. Devolver Filme")
        print("Opção 4. Sair")

        opcao = input("Escolha a opção desejada: ")

        if opcao == '1':
            minha_locadora.listar_catalogo()

        elif opcao == '2':
            titulo = input("Digite o título do filme: ")
            for filme in minha_locadora.catalogo:
                if filme.titulo == titulo:
                    resultado = filme.alugar()
                    print(resultado)
                    break
                else:
                    print(f"Filme '{titulo}' não encontrado na locadora.")

        elif opcao == "3":
            titulo = input("Digite o titulo do filme que deseja devolver: ")
            for filme in minha_locadora.catalogo:
                resultado = filme.devolver()
                print(resultado)
                break
            else:
                print(f"Filme '{titulo}' ") 

        elif opcao == "4":
            print("Encerrando aplicação")
            break
        
        else:
            print("Opção invalida!")

if __name__ == "__main__":
    main()



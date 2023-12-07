"""Crie uma função que cria um diretorio e pergunte ao usuario qual sera o nome"""
import os

"""def criar_diretorio():
    nome_diretorio = input("Qual será o nome para o diretório?")

    #Criar o diretorio
    novo_diretorio = os.path.join(os.getcwd(), nome_diretorio)
    
    #Criando um novo diretorio

    os.mkdir(novo_diretorio)

    print(f"Diretório '{nome_diretorio}' criado com sucesso! \n")

criar_diretorio()"""

#mover ou renomear um arquivo
caminho_antigo = "A:\\Prof. Cassio de Albuquerque\\Python III\\Marco\Aula 20 - OS\\teste_nome.txt"

novo_caminho = "A:\\Prof. Cassio de Albuquerque\\Python III\\Marco\Aula 19\\mudei_de_nome.txt"

os.rename(caminho_antigo, novo_caminho)

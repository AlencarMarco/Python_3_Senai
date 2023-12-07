"""crie uma função que peça para o usuario digitar o caminho de uma pasta/diretorio
e liste os arquivos utilizando a biblioteca OS"""
import os
    

def listar_arquivos():
    caminho_diretorio = input("Informe o caminho do diretorio: ")

    #listar os arquivos do diretorio passado
    arquivos = os.listdir(caminho_diretorio)
    print("Os arquivos do diretorio passado são: ")

    for arquivo in arquivos:
        print(arquivo)

    else: 
        print("Diretorio invalido")

    
listar_arquivos()

    
    

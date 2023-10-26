from filme import Filme, Serie, Documentario
from cliente import Cliente
from login import Login
from conta import Conta
from cadastro import Cadastro

print("#####################################")
print("       Welcome to SenaiFlix          ")
print("#####################################")

clientes = {}
titulos = {}

while True:
    print("Escolha uma opção: ")
    print("Opção 1. Alugar um Filme")
    print("Opção 2. Alugar uma Serie")
    print("Opção 3. Alugar um Documentario")
    print("Opção 4. Deletar Títulos")
    print("Opção 5. sair")

    opcao = int(input("Digite a opção: \n"))
    
    if opcao == 5:
        break

    elif opcao == 1:
        while True:
            opcao = int(input("Digite a opção: \n"))
            print("Escolha uma opção: ")
            print("Opção 1. Alugar um Filme")
            print("Opção 2. Alugar uma Serie")
            print("Opção 3. Alugar um Documentario")
            print("Opção 4. sair")
           
            if opcao == 4:
                break

            if opcao == 1:
                cadastro = Cadastro()
                cadastro.verifica_Cadastro()
                print(input("Digite a opção do filme: "))
                

            

    
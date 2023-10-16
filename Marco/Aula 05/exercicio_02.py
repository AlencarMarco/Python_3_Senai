"""Crie um programa: Lista de tarefas, crie um menu: Incluir tarefas, excluir, ordenar, contar o numero de tarefas, sair"""

lista_Tarefas = []
print("########### MINHA LISTA DE TAREFAS PESSOAIS ###############")
print("###############################################")

while(True):
    print("Escolha uma opção \n")
    print("Opção 01: Adicionar uma tarefa \n")
    print("Opção 02: Excluir uma tarefa \n")
    print("Opção 03: Verificar a quantidade de tarefas \n")
    print("Opção 04: Listar Tarefas\n")
    print("Opção 05: Sair \n")
  
    opcao = int(input())

    if(opcao == 1):
        tarefa = input("Digite a tarefa: ")   

        lista_Tarefas.append(tarefa)
        print(lista_Tarefas)

    elif(opcao == 2):       
        tarefa_off = input("Digite a tarefa para excluir:")
        lista_Tarefas.remove(tarefa_off)
        print(lista_Tarefas)

    elif(opcao == 3):
        tamanho = len(lista_Tarefas) # Retorna a quantidade de itens na lista
        print(f"Você tem {tamanho} tarefas na sua lista de tarefas")


    elif(opcao == 4):
        print(lista_Tarefas)

    elif(opcao == 5):
      break

    



       
    
    

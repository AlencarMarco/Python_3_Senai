"""Criar um programa de controle de estoque, criar, ler, atualizar, excluir - CRUD(Creat/ Read/ Update/ Delete)
Dicionario vazio - Estoque

"""
"""from layout import menu_2

estoque = {}

  while(True):
    print("Escolha uma opção \n")
    print("Opção 1: Inserir \n")
    print("Opção 2: Ler \n")
    print("Opção 3: Atualizar \n")
    print("Opção 4: Excluir \n")
    print("Opção 5: Sair \n")
  
    opcao = int(input())

    if (opcao == 5):
        
        break

    elif(opcao == 1):
       nome = input("Digite o nome do contato \n")
       estoque['nome_item'] = nome
       
       quantidade = int (input( "Digite o nome do item: \n"))                    
       estoque['quantidade_item'] = quantidade 
       
       print(f"Utem {nome} adicionado com sucesso")
       print(estoque)
       

    elif(opcao == 2):
        for contato in agenda:
              print(contato)     
        

    elif(opcao == 3):
        busca = input("Digite o nome do contato \n")
        for nome in agenda:
            print(nome) 

    else:
        print("Tente novamente")"""



estoque = {}

def create (codigo, nome, quantidade):
    codigo = int (input("Digite o codigo: "))
    if codigo not in estoque:
        estoque [codigo] = {'nome' : nome, 'quantidade' : quantidade}

    else:
        print("O item já existe no estoque. Use a função atualizar_item para modificar a quantidade. ")

def upd (codigo, nome, quantidade):
    if codigo in estoque:
        estoque [codigo] ["quantidade"] =  quantidade

    else:
        print ("O item não existe no estoque. Use fução incluir_item para adiciona-lo")
        
def read (codigo, nome, quantidade):
    if codigo in estoque:
        for i in estoque:
            print (i, '\n')
    
    else:
        print ("O item não existe no estoque. Use fução incluir_item para adiciona-lo")

def delete (codigo, nome, quantidade):
    if codigo in estoque:
        del estoque ["codigo"] ["nome"] ["quantidade"]

    else:
        print ("O item não existe no estoque. Use fução incluir_item para adiciona-lo")

def menu():
    while (True): 
        print ("Escolha uma opção: \n")
        print ("Opção 1 : Adicionar um produto \n")
        print ("Opção 2: Ler um produto \n")
        print ("Opção 3: Atualizar o estoque \n")
        print ("Opção 4: Excluir um produto do estoque \n")
        print ("Opção 5: Sair \n")

        opcao = int(input())

        if (opcao == 1):
            create ('codigo', 'nome', 'quantidade')
            print (estoque)
            
        '''elif (opcao == 2):
            
        elif (opcao == 3):

        elif (opcao == 4):
            
        elif (opcao == 5):
            print ("Você saiu")
            break

         else:
                print ("Opção incorreta")'''
        
menu()



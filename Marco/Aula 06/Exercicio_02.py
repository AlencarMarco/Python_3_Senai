"""Crie, dicionario chamado "contatos" nesse dicionario, tenha as Chaves: nome, telefone, e-mail e endereço.
com 5 contatos
2º etapa 
Padrão de projeto com menu.
Agenda de contatos, usuario digitar os dados(Nome e telefone), listar os contatos, e Buscar um contato"""

print("########### MINHA AGENDA PESSOAL ###############")
print("###############################################")

agenda = []

while(True):
    print("Menu \n")
    print("Opção 01: ADICIONAR UM CONTATO \n")
    print("Opção 02: LISTAR OS CONTATOS \n")
    print("Opção 03: BUSQUE UM CONTATO \n")
    print("Opção 04: Sair \n")
  
    opcao = int(input())

    if(opcao == 1):
       nome = input("Digite o nome do contato \n")
       telefone = int (input( "Digite o número de telefone: \n"))                    
       contato = {'nome':nome, 'telefone':telefone}
       agenda.append(contato)
       print(f"Contato {nome} adicionado com sucesso")
       print(agenda)
       

    elif(opcao == 2):
        for contato in agenda:
              print(contato)     
        

    elif(opcao == 3):
        busca = input("Digite o nome do contato \n")
        for nome in agenda:
            print(nome)


           

    #elif(opcao == 4):



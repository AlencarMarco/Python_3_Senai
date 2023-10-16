num1 = 0
num2 = 0

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def dividir(num1, num2):
    return num1 / num2

def multiplicar(num1, num2):
    return num1 * num2


def menu():
  while(True):
    print("Escolha uma opção \n")
    print("Opção 1: Adição \n")
    print("Opção 2: Subtração \n")
    print("Opção 3: Multiplicação \n")
    print("Opção 4: Divisão \n")
    print("Opção 5: Sair \n")
  
    opcao = int(input())

    print("Escolha os dois numeros da operação \n")    

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if (opcao == 5):
        
        break

    elif(opcao == 1):
     
     print("O resultado da operação é", somar(num1, num2), "\n")

    elif(opcao == 2):
       
       print(subtrair(num1, num2))

    elif(opcao == 3):
       
        print(multiplicar(num1, num2))

    elif(opcao == 4):
        
        print(dividir(num1, num2)) 

    else:
        print("Tente novamente")

def menu_2():
  while(True):
    print("Escolha uma opção \n")
    print("Opção 1: Inserir \n")
    print("Opção 2: Ler \n")
    print("Opção 3: Atualizar \n")
    print("Opção 4: Excluir \n")
    print("Opção 5: Sair \n")
  
    opcao = int(input())

    print("Escolha os dois numeros da operação \n")    

    if (opcao == 5):
        
        break

    elif(opcao == 1):
       nome = input("Digite o nome do contato \n")
       
       quantidade = int (input( "Digite o nome do item: \n"))                    
       contato = {'nome':nome, 'telefone':telefone}
       
       print(f"Contato {nome} adicionado com sucesso")
       print(agenda)
       

    elif(opcao == 2):
        for contato in agenda:
              print(contato)     
        

    elif(opcao == 3):
        busca = input("Digite o nome do contato \n")
        for nome in agenda:
            print(nome) 

    else:
        print("Tente novamente")
   



    
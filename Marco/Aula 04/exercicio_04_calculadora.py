#utilizando while, if, elif, flot = crie uma calculadora com opções matematicas e uma opção para sair


while(True):
    print("Escolha uma opção \n")
    print("Opção 1: Adição \n")
    print("Opção 2: Subtração \n")
    print("Opção 3: Multiplicação \n")
    print("Opção 4: Divisão \n")
    print("Opção 5: Sair \n")
  
    opcao = int(input())

    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))

    if (opcao == 5):
        break

    elif(opcao == 1):
        
        print(numero_1)
        print(numero_2)

        adicao = numero_1 + numero_2

        print("Esse é o resultado da sua Adição:" , adicao)

    elif(opcao == 2):
        
        print(numero_1)
        print(numero_2)

        subtracao = numero_1 - numero_2

        print("Esse é o resultado da sua Subtração:" , subtracao)

    elif(opcao == 3):
        
        print(numero_1)
        print(numero_2)

        multiplicacao = numero_1 * numero_2

        print("Esse é o resultado da sua Multiplicação:" , multiplicacao)

    elif(opcao == 4):
        
        print(numero_1)
        print(numero_2)

        divisao = numero_1 - numero_2

        print("Esse é o resultado da sua Divisão:" , divisao)  

    else:
        print("Obrigado")
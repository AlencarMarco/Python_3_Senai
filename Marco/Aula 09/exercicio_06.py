"""Neste projeto, você pode criar uma calculadora interativa que utiliza a calsse Calculadora para realizar operações"""
#utilizando while, if, elif, flot = crie uma calculadora com opções matematicas e uma opção para sair
from exercicio_01 import Calculadora

calculadora = Calculadora() #Criar o objeto para calcular

while(True):
    print("Escolha uma opção \n")
    print("Opção 1: Adição \n")
    print("Opção 2: Subtração \n")
    print("Opção 3: Multiplicação \n")
    print("Opção 4: Divisão \n")
    print("Opção 5: Sair \n")
  
    opcao = int(input())

    if (opcao == 5):
        break
    
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
   
  
    if(opcao == 1):
        print(calculadora.somar(a,b))

    elif(opcao == 2):
        print(calculadora.subtrair(a,b))

    elif(opcao == 3):
        print(calculadora.multiplicar(a,b))

    elif(opcao == 4):
        print(calculadora.dividir(a,b))






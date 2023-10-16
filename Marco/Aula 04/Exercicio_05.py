"""usuario digita um numero e o contador conta todos os numeros impares e pares até o numero digitado"""

"""numero = float(input("Digite um número: \n"))
contador_par=0
contador_impar=0
indice = 1


while indice <= numero:

  if(numero % 2 == 0):
     contador_par += 1
     print(f"de 1 até {numero} temos {contador_par} numeros pares...")

  else:
    contador_impar += 1
    indice += 1
    print(f"de 1 até {numero} temos {contador_impar} numeros pares...")

    break"""



numero = float(input("Digite um número:"))

contador_par=0
contador_impar=0

while(True):
    if numero % 2 == 0:
        print(f"De 1 até {numero} temos {contador_par + 1} números pares.")
    else:
       print(f"De 1 até {numero} temos {contador_impar +1} números impares")

    break     


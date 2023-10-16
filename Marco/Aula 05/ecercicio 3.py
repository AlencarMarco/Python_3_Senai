"""Programa que o usuario adiciona numeros, e retorne a média dos numeros digitados"""

"""lista = []

numero_1 = float(input("Digite o seu 1º número: "))
lista.append(numero_1)

numero_2 = float(input("Digite o seu 2º número: "))
lista.append(numero_2)

numero_3 = float(input("Digite o seu 3º número: "))
lista.append(numero_3)

numero_4 = float(input("Digite o seu 4º número: "))
lista.append(numero_4)

numero_5 = float(input("Digite o seu 5º número: "))
lista.append(numero_5)

soma = sum(lista)
quantidade = len(lista)

media = soma / quantidade

print("Essa é a Media dos numeros inserido: " , media)"""




while(True):
    lista = []
    quantidade = len(lista)

    if quantidade <1:
      numero_1 = int(input("Digite o seu 1º número: "))

      lista.append(numero_1)
      print(lista)

    elif quantidade >1:
      numero_2 = int(input("Digite o seu 1º número: "))

      lista.append(numero_2)
      print(lista)    

    elif quantidade >= 5:
      soma = sum(lista)
      quantidade = len(lista)

      media = soma / quantidade

      print("Essa é a Media dos numeros inserido: " , media)

      break
        





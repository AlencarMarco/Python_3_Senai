#programa para validar se um numero é par ou impar utilizando %

numero_usuario = int (input("Digite o número: "))

if ( numero_usuario % 2 == 0):
    print(numero_usuario, " é par")

else:
    print(numero_usuario, "é impar")

def contar_pares_impares(numero):
    pares = 0
    impares = 0
    i = 1

    while i <= numero:
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
        i += 1

    return pares, impares

try:
    numero = int(input("Digite um número: "))
    if numero < 1:
        print("Por favor, digite um número maior ou igual a 1.")
    else:
        pares, impares = contar_pares_impares(numero)
        print(f"Números pares: {pares}")
        print(f"Números ímpares: {impares}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

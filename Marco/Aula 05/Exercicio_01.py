"""Desafio 01: Crie uma lista, qualquer, e some os elementos da lista, coloque o valor maximo e o valor minimo, depois ordene a lista """

lista = [10,30,20,25,12.6,20.9,54.20]

lista.sort()
print(lista)

soma = sum(lista)
print("Aqui esta a soma da sua lista :", soma)

maximo = max(lista) #aponta o mair numero da lista, é necessário criar uma variavel para utilizar a função.
print("Esse é o valor maximo da sua lista: " , maximo)

minimo = min(lista)
print("Esse é o valor minimo da sua lista: " , minimo)

for i in lista:
    if i % 2 == 0:
        print(i)









"""Diciconario, """

contato = {
    {"Nome": "Cassio",
    "Telefone": 123456,
    "e-mail": "cassio@cassio"},

print(contato ["Nome"])

contato["endereço"] = "rua teste do meu endereço" #Adiciona  um dado ao dicionario.


print(contato)

valor = contato["Nome"]

print(valor)

contato['Nome'] = "Mario" #Altera a chave de um item do dicionario

print(contato['Nome'])

# del contato['Nome'] #Deleta um elemento

if 'endereço' in contato:
  print("Achei")

else:
  print("Tem Não")

for Nome in contato.items():
  print(contato['Nome'])





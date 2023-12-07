import os

#Exemplo 1: Obter o diretorio de trabalho Atual
diretorio_atual = os.getcwd()
print(f"O Diretorio atual é: {diretorio_atual}")

#Ex 2: Listar os arquivos em um Diretorio
diretorio = "A:\\Prof. Cassio de Albuquerque\Python III\Marco"
arquivos = os.listdir(diretorio)

print("Os arquivos do diretorio são:")
for arquivo in arquivos:
    if(arquivo == "Aula 01"):
        print(arquivos)
    else:
        print("Arquivo não encontrado")

#Criar um diretorio
novo_diretorio = "A:\\Prof. Cassio de Albuquerque\Python III\Marco"

os.mkdir(novo_diretorio)

#Executar comandos no sistema
contador = 0 

while contador < 10:
    os.system("echo Olá, mundo") #Echo - Usado muito em PHP, semelhante ao PRINT do phyton
    contador +- 1


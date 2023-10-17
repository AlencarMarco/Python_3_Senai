"""Crie uma classe, aluno - Tem que ter: nome, idade, e-mail - Metodo - Perguntar"""

class Aluno: #Essa é a forma do objeto
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email


    def aluno_pergunta(self, pergunta): #Esse é o Metodo do objeto
        
        pergunta = input("Digite a pergunta: ")
        print(pergunta)

aluno_01 =  Aluno()

aluno_01.aluno_pergunta()



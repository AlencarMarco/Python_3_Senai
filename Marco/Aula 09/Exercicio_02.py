"""Crie uma classe aluno que possui atributos como nome, idade e notas,. Implemente metodos para calcular a media das 
notas e verificar se o aluno foi aprovado(Media maior igual a 6)"""

class Aluno: #Essa é a forma do objeto
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcula_media(self, notas): #Esse é o Metodo do objeto
        return sum(self.notas) / len(self.notas)
    
    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 6:
            return f"{self.nome} foi aprovado"
        else: 
            return f"{self.nome} foi reprovado"
            
aluno01 = Aluno("Marco", 33, 7, 6, 3)
       
        
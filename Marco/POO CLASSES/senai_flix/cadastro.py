from cliente import Cliente
from login import Login

cadastro_cliente = {}

class Cadastro(Cliente):

    # def __init__(self, nome, endereco, email, senha):
    #     self.senha=senha
    #     super().__init__(nome, endereco, email)

    def efetuar_Cadastro(self):
    
        nome = input("Digite o seu nome: \n")
        endereco = input("Digite o seu endereço: \n")
        email = input("Digite o seu e-mail: \n")
        senha = int(input("Digite uma senha de 4 numeros: \n"))

        print(f"Bem vindo {nome}")
        print(cadastro_cliente [nome, endereco,email,senha])
        print(f"A senha cadastrada é {senha} memorize e não compartilhe com ninguem")

    def verifica_Cadastro(self):
        print("Você já possui cadastro?")
        print("Digite 'S' para sim e 'N' para não")
        resposta = input("Digite sua opção: ")

        if resposta == "S":
            from login import Login
            login1 = Login()
            login1.efetuar_login()

        if resposta == "N":
            cadastro1 = Cadastro()
            cadastro1.efetuar_Cadastro()
            

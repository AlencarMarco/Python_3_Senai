from cadastro import Cadastro
cadastro_cliente = {}

class Login:
    def __init__(self, email, senha):
        self.email= email
        self.senha= senha

    def efetuar_login(self, email, senha):
        from cadastro import Cadastro
        cadastro_01 = Cadastro()
        self.email= input("Digite o seu E-mail: ")
        self.senha= input("Digite a sua Senha: ")

        if (email == email): 
            if(senha == senha):
               print("Login efetuado com sucesso")
            else:
                print("E-mail ou senha errados")

        

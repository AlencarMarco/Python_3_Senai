class Contato:
    def _init_(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")


class ContaPessoal(Contato):
    def _init_(self, nome, telefone, aniversario):
        super()._init_(nome, telefone)
        self.aniversario = aniversario

    def apresentar(self):
        super().apresentar()
        print(f"Aniversário: {self.aniversario}")


class ContaProfissional(Contato):
    def _init_(self, nome, telefone, empresa):
        super()._init_(nome, telefone)
        self.empresa = empresa

    def apresentar(self):
        super().apresentar()
        print(f"Empresa: {self.empresa}")


# Exemplo de uso:
contato_pessoal = ContaPessoal("João","15 de janeiro")
contato_profissional = ContaProfissional("Maria","Acme Inc.")

print("Contato Pessoal:")
contato_pessoal.apresentar()

print("\nContato Profissional:")
contato_profissional.apresentar()
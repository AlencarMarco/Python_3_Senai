
class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self,contato):
        self.contatos.append(contato)
        
    def listar_contatos(self):
        print(f"Aqui estão os contatos:")
        for contato in self.contatos:
            print(contato)

    def buscar_contatos(self):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None
    
    def deletar_contatos(self, nome):
            contato = self.buscar_contatos
            if contato is not None:
                self.contatos.remove(contato)
                print(f"Contato {nome} removido da agenda")

            else: 
                print(f"Contato {nome} não encontrado na agenda")

def main():
    while True:
        print("Escolha uma opção")
        print("Opção 1 - Listar contatos")
        print("Opção 2 - Buscar contatos")
        print("Opção 3 - Remover contatos")
        print("Opção 4 - Sair")
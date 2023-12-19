import sqlite3

# Função para criar tabela
def criar_tabela():
    conn = sqlite3.connect('contatos.db')
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS   
                   contatos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome TEXT NOT NULL, telefone TEXT NOT NULL)
                    ''')
    
    conn.commit()
    conn.close()

# Função para adicionar um novo contato
def adicionar_contato(nome, telefone):
    conn = sqlite3.connect('contatos.db')
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO contatos(nome, telefone) VALUES (?, ?)''', (nome, telefone))

    conn.commit()
    conn.close()

# Função para obter dados do contato
def obter_dados():
    conn = sqlite3.connect('contatos.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM contatos''')

    contatos = cursor.fetchall()
    conn.close()

    return contatos

# Função para atualizar contatos
def atualizar_contato(contato_id, novo_nome, novo_telefone):
    conn = sqlite3.connect('contatos.db')
    cursor = conn.cursor()

    cursor.execute('''UPDATE contatos SET nome = ?, telefone = ? WHERE id = ?''', (novo_nome, novo_telefone, contato_id))

    conn.commit()
    conn.close()

# Função para excluir contato
def excluir_contato(contato_id):
    conn = sqlite3.connect('contatos.db')
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM contatos WHERE id = ?''', (contato_id,))
    conn.commit()
    conn.close()

# Função principal
def main():
    criar_tabela()

    while True:
        print("\n Menu")
        print("1. Adicionar Contatos ")
        print("2. Listar Contatos")
        print("3. Atualizar Contatos")
        print("4. Excluir Contatos")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone: ")
            adicionar_contato(nome, telefone)
            print("Contato adicionado com sucesso!")
        
        elif escolha == "2":
            contatos = obter_dados()
            print("\n Lista de contatos:")
            for contato in contatos:
                print(f"{contato[0]}. Nome: {contato[1]}. Telefone: {contato[2]}")

        elif escolha == "3":
            contato_id = input("Digite o id do contato que deseja atualizar: ")
            novo_nome = input("Digite o novo nome: ")
            novo_telefone = input("Digite o novo telefone: ")

            atualizar_contato(contato_id, novo_nome, novo_telefone)

            print("Contato atualizado com sucesso!")

        elif escolha == "4":
            contato_id = input("Digite o id do contato que deseja excluir: ")
            excluir_contato(contato_id)
            print("O contato foi excluído com sucesso!")
            
        elif escolha == "5": 
            print("Saindo do programa")
            break

if __name__ == "__main__":
    main()

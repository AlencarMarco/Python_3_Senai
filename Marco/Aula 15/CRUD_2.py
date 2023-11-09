import mysql.connector 

#conectar ao banco de dados

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'senai',
    database = 'loja_ii'
    )

cursor = conn.cursor()

#Criar uma tabela chamda cliente_vip

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cliente_vip (
            idcliente INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(45) NOT NULL,
            endereco VARCHAR(255) NOT NULL,
            telefone INT(13),
            email VARCHAR(45) NOT NULL,
            cpf INT(20) NOT NULL 
            )''')

#Função para inserir dados na tabela clientes_vip
def inserir_clientes(nome, endereco, telefone, email, cpf):
        query = 'INSERT INTO cliente_vip(nome, endereco, telefone, email, cpf) VALUES (%s, %s, %s, %s, %s,)'
        values = (nome, endereco, telefone, email, cpf)
        cursor.execute(query, values)
        conn.commit()

#função para listar todos os clientes

def listar_clientes():
    cursor.execute('SELECT * from clientes_vip')
    cliente = cursor.fetchall()
    for clientes in cliente:
        print(clientes)

#função para atualizar a tabela _clienteVip

def atualizar_clientes_vip(idcliente, nome,endereco, telefone,email,cpf):
    query = "UPDATE cliente_vip SET nome = %s, endereco = %s, telefon = %s, email = %s,cpf = %s WHERE idcliente = %s"
    values = (nome, endereco, telefone, email, cpf, idcliente)
    cursor.execute(query, values)

#Função para deletetar um cliente

def delete_cliente(idcliente):
    query = 'DELETE FROM cliente_vip WHERE idcliente = %s'
    values = (idcliente)
    cursor.execute(query,values)

#exemplo de uso, inserir um cliente

inserir_clientes('Marco', 'Rua do Batman', '123456789', 'marco@gmail', '321654987')

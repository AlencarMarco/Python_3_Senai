
import pandas as pd

#Criação do Dataframe


# Dados fictícios dos alunos
dados_alunos = {
    'Nome': ['João', 'Maria', 'Carlos', 'Ana'],
    'Idade': [18, 20, 19, 22],
    'Nota_Matematica': [90, 85, 88, 92],
    'Nota_Portugues': [78, 80, 75, 85]
}

# Criar o DataFrame
df_alunos = pd.DataFrame(dados_alunos)

# Exibir o DataFrame
print(df_alunos)
###############################################
#Análise de Dados:
#Faça algumas análises básicas usando Pandas.

# Média das notas em Matemática e Português
media_matematica = df_alunos['Nota_Matematica'].mean()
media_portugues = df_alunos['Nota_Portugues'].mean()

# Imprimir a média
print(f'Média em Matemática: {media_matematica}')
print(f'Média em Português: {media_portugues}')

#Este trecho de código calcula e imprime a média das notas em Matemática e Português
#####################################

#Visualização de Dados:
#Utilize a biblioteca matplotlib para visualizar as notas dos alunos.

import matplotlib.pyplot as plt

# Gráfico de barras das notas em Matemática
df_alunos.plot(x='Nome', y=['Nota_Matematica', 'Nota_Portugues'], kind='line')
plt.title('Notas dos Alunos em Matemática e Português')
plt.xlabel('Aluno')
plt.ylabel('Nota')
plt.show()
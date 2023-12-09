import pandas as pd
import matplotlib.pyplot as plt

#Lista de vendedores

ranking_vendas = {
    "Vendedor": ["João","Marcelo", "Paulo","Felipe", "Thais"],
    "Valor_Vendido":[10000.00, 500.00, 7800.00, 5800.00, 6000.00],
    "Conversao_Vendas":[2000, 3000, 1000, 5000, 3000]
}

#Criar seu dataframe
df = pd.DataFrame(ranking_vendas)

print(df)

media_vendas = df['Valor_Vendido'].mean()
media_conversao = df['Conversao_Vendas'].mean()
maximo_venda = df['Valor_Vendido'].max()
maximo_venda = df['Valor_Vendido'].min()

print(media_vendas)
print(media_conversao)
print(maximo_venda)

# Gráfico de barras das notas em Matemática
df.plot(x='Vendedor', y=['Valor_Vendido', 'Conversao_Vendas'], kind='bar')

plt.title('Ranking de Vendas')

plt.xlabel('Vendedores')
plt.ylabel('Vendas')
plt.show()



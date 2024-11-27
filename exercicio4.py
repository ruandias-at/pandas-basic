import pandas as pd

df = pd.read_excel("dados_exemplo.xlsx")

#Agrupar por Produto e calcular a soma das quantidades vendidas
total_vendido_por_produto = df.groupby('Produto', as_index=False)['Quantidade'].sum()

#Renomear a coluna para deixar claro que é o total vendido
total_vendido_por_produto.rename(columns={'Quantidade': 'Total Vendido'}, inplace=True)

#Exibir o resultado
print(total_vendido_por_produto)

import pandas as pd

df = pd.read_excel("dados_exemplo.xlsx")

#Filtrar vendas com Receita Total acima de 15 reais
vendas = df[df['Receita Total'] > 15]

#Exibir o resultado
print(vendas)
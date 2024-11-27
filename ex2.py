import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados da planilha
dados_vendas = pd.read_excel("dados_vendas.xlsx")

# Converter a coluna 'Data' para o formato datetime (garantindo que funcione com .dt.year)
dados_vendas['Data'] = pd.to_datetime(dados_vendas['Data'], format='%d/%m/%Y')

# Escolher o ano para análise
ano_escolhido = 2023

# Filtrar os dados para o ano escolhido
dados_ano = dados_vendas[dados_vendas['Data'].dt.year == ano_escolhido]

# Agrupar as vendas por categoria para o ano escolhido
vendas_por_categoria = dados_ano.groupby('Categoria')['Total_Venda'].sum().reset_index()

# Gráfico de Barras
plt.figure(figsize = (10, 6))
plt.bar(vendas_por_categoria['Categoria'], vendas_por_categoria['Total_Venda'], color = 'blue')
plt.title(f"Vendas Totais por Categoria de Produto em {ano_escolhido}")
plt.xlabel("Categoria de Produto")
plt.ylabel("Total de Vendas")
plt.xticks(rotation = 45) # Rotaciona os rótulos do eixo X para facilitar a leitura
plt.tight_layout()
plt.show()
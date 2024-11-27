import pandas as pd # Importa a biblioteca pandas, útil para manipulação de dados em formato de tabela
import matplotlib.pyplot as plt # Importa a biblioteca matplotlib para criar gráficos

# Carregar os dados da planilha
dados_vendas = pd.read_excel("dados_vendas.xlsx") # Lê o arquivo Excel "dados_vendas.xlsx" e armazena os dados em um DataFrame

# Converter a coluna 'Data' para o formato datetime
dados_vendas['Data'] = pd.to_datetime(dados_vendas['Data'], format='%d/%m/%Y')# Converte a coluna 'Data' para o formato datetime, usando o formato dia/mês/ano

# Extrair ano e mês para a análise
dados_vendas['Ano'] = dados_vendas['Data'].dt.year # Extrai o ano da coluna 'Data' e armazena em uma nova coluna 'Ano'
dados_vendas['Mes'] = dados_vendas['Data'].dt.month # Extrai o mês da coluna 'Data' e armazena em uma nova coluna 'Mes'

# Agrupar os dados por ano e mês, e calcular o total de vendas
vendas_mensais = dados_vendas.groupby(['Ano', 'Mes'])['Total_Venda'].sum().reset_index()# Agrupa os dados pelo ano e mês, somando as vendas em 'Total_Venda' para cada grupo; o reset_index organiza o resultado em uma tabela clara

# Criar o gráfico com linhas separadas para cada ano
plt.figure(figsize=(12, 6)) # Define o tamanho do gráfico em polegadas: 12 de largura e 6 de altura
for ano in vendas_mensais['Ano'].unique(): # Loop para criar uma linha separada para cada ano
    dados_ano = vendas_mensais[vendas_mensais['Ano'] == ano] # Filtra os dados para o ano atual no loop
    plt.plot(dados_ano['Mes'], dados_ano['Total_Venda'], marker='o', label=str(ano))# Plota a linha de vendas mensais para o ano atual, com um marcador em círculo em cada ponto

# Ajustes do gráfico
plt.title("Tendência Mensal de Vendas ao Longo dos Anos") # Define o título do gráfico
plt.xlabel("Mês") # Define o rótulo do eixo X
plt.ylabel("Total de Vendas") # Define o rótulo do eixo Y
plt.xticks(range(1, 13), ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']) # Configura os rótulos do eixo X como os nomes dos meses
plt.yticks(range(0, int(vendas_mensais['Total_Venda'].max()) + 5000, 5000)) #Configura o intervalo do eixo Y em incrementos de 5000
plt.legend(title="Ano") # Adiciona uma legenda ao gráfico, com o título "Ano"
plt.tight_layout() # Ajusta automaticamente os elementos do gráfico para caberem bem no espaço
plt.show() # Exibe o gráfico
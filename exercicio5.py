import pandas as pd

df = pd.read_excel("dados_exemplo.xlsx")

#Solicitar o nome do aluno que o usuário deseja buscar
nome_aluno = input("Digite o nome do aluno que deseja buscar: ")

#Filtrar pelo nome do aluno inserido pelo usuário
aluno_filtrado = df[df['Nome'] == nome_aluno]

#Verificar se o aluno foi encontrado
if not aluno_filtrado.empty:
    #Agrupar pelos produtos, somar as quantidades e manter o preço unitário
    produtos_agrupados = aluno_filtrado.groupby('Produto', as_index=False).agg({
        'Quantidade': 'sum',
        'Preço Unitário': 'first' #Mantém o preço unitário do primeiro registro do produto
    })

    #Calcular o total gasto por produto (Quantidade * Preço Unitário)
    produtos_agrupados['Total'] = produtos_agrupados['Quantidade'] * produtos_agrupados['Preço Unitário']

    #Exibir as informações do aluno e o total de cada produto comprado com preço unitário e total gasto
    print(f"Informações do aluno '{nome_aluno}':")
    print(aluno_filtrado)
    print("\nResumo de cada produto comprado pelo aluno:")
    print(produtos_agrupados)
else:
    print(f"Nenhum aluno com o nome '{nome_aluno}'.")
import pandas as pd
#Exemplo de dataframe simples
df = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'idade': [23, 35, 45, 29, 41],
    'email': ['ana@example.com', 'bruno@example.com', 'carlos@example.com', 'daniela@example.com', 'eduardo@example.com']
})

#Selecionar a coluna 'idade' se for maior que 30 e 'nome' se começar com 'C'
filtro = df[(df['idade'] > 30) & (df['nome'].str.startswith('C'))]
print(filtro)

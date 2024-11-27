import pandas as pd
#Exemplo de dataframe simples
df = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'idade': [23, 35, 45, 29, 41],
    'email': ['ana@example.com', 'bruno@example.com', 'carlos@example.com', 'daniela@example.com', 'eduardo@example.com']
})

#Selecionar a coluna 'idade' se for maior que 30
acima_de_30 = df[df['idade'] > 30]
print(acima_de_30)

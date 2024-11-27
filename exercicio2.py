import pandas as pd

df = pd.read_excel("dados_exemplo.xlsx")

#Agrupar por curso e calcular a média das notas
media_notas_por_curso = df.groupby('Curso', as_index=False)['Nota Final'].mean()

#Renomear a coluna para indicar que é a média
media_notas_por_curso.rename(columns={'Nota Final': 'Média Nota Final'}, inplace=True)

#Exibir o resultado final
print(media_notas_por_curso)
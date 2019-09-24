import numpy as np
import pandas as pd

# Inicializando Series
series = pd.Series(data=[45000, 170000], index=["PR", "SP"])

# Inicializando DataFrame
df = pd.DataFrame(data=np.random.randn(5, 4), index="A B C D E".split(), columns="W X Y Z".split())

# Criando nova coluna somando duas já existentes
df['new column'] = df['W'] + df['Z']

# Apagando coluna
df.drop('new column', axis=1, inplace=True)

# Seleção de dado
loc = df.loc[['A', 'B']]
loc = df.loc[['D', 'E'], ['X', 'Y']]

# Seleção de dado com condicional
cond = df[(df['W'] > 0) & (df['X'] < 1)]

# Tratamento de valores nulos (filtrando e substituindo por 0)
d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df1 = pd.DataFrame(d)
df1.fillna(value=0, inplace=True)

# Utilizando GroupBy
data = {
    'Empresa': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'Nome': ['San', 'Charlie', 'Any', 'Vanessa', 'Carl', 'Sarah'],
    'Venda': [200, 120, 340, 124, 243, 350]
}
df2 = pd.DataFrame(data)
group = df2.groupby('Empresa')
sum = group.sum()
describe = group.describe()

# Selecionar dados não repetidos
data = df2['Empresa'].unique()

# Executar uma função em cada elemento da coluna
func = df2['Venda'].apply(lambda x: x/2)

# Ordenar colunas
df2.sort_values(by='Empresa', inplace=True)

# Leitura e envio de arquivo CSV
df3 = pd.read_csv('exemplo.csv', sep=';')
#df3.to_csv("exemplo.csv", sep=';', decimal=',')

# Leitura e envio de arquivo Excel
df3 = pd.read_excel('Exemplo_Excel.xlsx', sheet_name='Sheet1')
#df3.to_excel('Exemplo_Excel.xlsx', sheet_name='Sheet1')

# Leitura de arquivo HTML
#df3 = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')


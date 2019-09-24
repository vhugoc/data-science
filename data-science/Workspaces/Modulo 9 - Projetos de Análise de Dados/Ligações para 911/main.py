import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('911.csv')

# Separar as razões das ligações de acordo com o título em uma nova coluna
df['reason'] = df['title'].apply(lambda title: title.split(':')[0])

# Encontrar a quantidade de valores no agrupamento
qt_reason = df['reason'].value_counts()

# Countplot exibindo a quantidade de chamadas separadas pela razão
# sns.countplot(x='reason', data=df, palette='magma')

# Converter a coluna string timeStamp para datetime
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# Criar novas colunas com hora, dia da semana e mês
df['hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['dayofweek'] = df['timeStamp'].apply(lambda x: x.dayofweek)
df['month'] = df['timeStamp'].apply(lambda x: x.month)

# Mapear a coluna dayofweek para alterar os nomes dos dias da semana
dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
df['dayofweek'] = df['dayofweek'].map(dmap)

# Countplot dos dias da semana baseados na razão
# sns.countplot(x=df['dayofweek'], data=df, hue=df['reason'], palette='magma')

# Countplot dos meses baseados na razão
# sns.countplot(x=df['month'], data=df, hue=df['reason'], palette='magma')

# GroupBy nos dados do dataframe capturando a quantidade de cada um por mês
byMonth = df.groupby('month').count()

# Plot nas chamadas por mês
# byMonth['twp'].plot()

# Passar o mês como coluna e não como índice
byMonth.reset_index()

# lmplot de numeros de chamada por mês
# sns.lmplot(x='month', y='twp', data=byMonth.reset_index())

# Criar coluna 'date' contendo a data da coluna 'timeStamp'
df['date'] = df['timeStamp'].apply(lambda x: x.date())

# GroupBy e exibição de gráfico com a contagem de chamadas por dia
#df.groupby('date').count()['twp'].plot()

# Gerar 3 gráficos como o de cima mas separando-os pela razão
# Traffic
# df[df['reason'] == 'Traffic'].groupby('date').count()['twp'].plot()
# Fire
# df[df['reason'] == 'Fire'].groupby('date').count()['twp'].plot()
#EMS
# df[df['reason'] == 'EMS'].groupby('date').count()['twp'].plot()

# Criar novo dataframe agrupados por colunas de horas e indices de dias
dayHour = df.groupby(by=['dayofweek', 'hour']).count()['twp'].unstack()

# Criar heatmap com o dataframe acima
plt.figure(figsize=(12, 6))
sns.heatmap(dayHour, cmap='coolwarm')

plt.show()

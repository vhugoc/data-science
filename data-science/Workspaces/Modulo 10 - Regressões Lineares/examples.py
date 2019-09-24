import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importar metodo que faz o split(divisão dos dados) em treino e teste
# Este método divide em dois os dados onde uma parte é o conjunto de treino e a outra é o conjunto de teste
# O método faz o programa aprender com o conjunto de treino e testar com o conjunto de teste
from sklearn.model_selection import train_test_split

# Importar classe para a instância do modelo linear
from sklearn.linear_model import LinearRegression
lm = LinearRegression()

USAHousing = pd.read_csv('USA_Housing.csv')

# Definir parâmetros (o que vai predizer o modelo)
x = USAHousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]

# Definir o que será predito (nesse caso o preço)
y = USAHousing['Price']

# Este método retorna uma tupla com o formato abaixo
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)

# Captura os parâmetros do modelo linear passando o X de treino e Y de treino
# É necessário para inicializar o modelo
lm.fit(x_train, y_train)

coefs = pd.DataFrame(lm.coef_, x.columns, columns=['Coefs'])

# Prever algum dado
predict = lm.predict(x_test)

sns.distplot(y_test-predict)

plt.show()

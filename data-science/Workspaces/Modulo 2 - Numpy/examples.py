import numpy as np

lista = [1, 2, 3]

# Exemplo de criação array predefinido
array = np.array(lista)

# Criação de vetor/matriz zeros
zeros = np.zeros((2, 2))

# Criação de vetor/matriz ones
ones = np.ones((2, 2))

# Criação de vetor/matriz randomica
rd = np.random.rand(2, 2)

# Redefinir dimensão de um vetor/matriz já definida
reshape = rd.reshape(4)

# Verificar tamanho do vetor/matriz
length = rd.shape

# Encontrar menor e maior valor
min = reshape.min()
max = reshape.max()

# Encontrar indice do menor e maior valor
index_min = reshape.argmin()
index_max = reshape.argmax()

# Criação de array automático de 0 a 30 de 3 em 3
arr = np.arange(0, 30, 3).reshape(2, 5)

# Capturar valores com eficiência (todas as linhas até a coluna 3)
arr2 = arr[:, :3]

# Extrair informações a partir de uma decisão
bol = arr > 15
info = arr[bol] #info = todos os valores maiores que 15

# Exemplo para retornar valores desejados
arr3 = np.linspace(0, 100, 30).reshape(10, 3)
print(arr3[2:4, 1])

# Média
med = np.mean(arr3)
# Desvio Padrão
dp = np.std(arr3)
# Seno de todos os valores
sin = np.sin(arr3)

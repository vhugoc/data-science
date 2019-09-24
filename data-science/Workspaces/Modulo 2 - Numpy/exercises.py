# Importar
import numpy as np

# Criar array de zeros
zeros = np.zeros(10)

# Criar array de ones
ones = np.ones(10)

# Criar array de fives
fives = np.ones(10) * 5

# Criar array de 10 até 50
arr = np.arange(10, 51)

# Criar array dos pares de 10 até 50
pairs = list(filter(lambda var: var % 2 == 0, arr))

# Criar matriz 3x3 de valores variando de 0 até 8
mat = np.arange(0, 9).reshape(3, 3)

# Criar matriz identidade 3x3
mat = np.eye(3, 3)

# Somando matrizes randomicas e em ordem crescente
arr = np.sort(np.random.rand(2, 3)) * 100
arr2 = np.sort(np.random.rand(2, 3)) * 100
sum = arr + arr2

print("Array 1: {}\n\nArray 2: {}\n\nSoma: {}" .format(arr, arr2, sum))

# Exemplo Lista
lista = [1, 2, 3, 4, 5]

# Exemplo Dicionário
dic = {'nome': "Victor", 'idade': 18}


# Exemplo Tupla
tup = (1, 2, 3)


# Exemplo For
for item in lista:
    print(item)


# Exemplo While
i = 0
while i < len(lista):
    print("Posição {position} = {value}" .format(position=i, value=lista[i]))
    i += 1


# Criar lista a partir de um for em uma linha
lista2 = [item**2 for item in lista]


# Exemplo Função
def soma(n1,n2):
    return n1+n2


# Exemplo função lambda
lambda var: var ** 2


# Exemplo map (cria uma lista executando uma função em todos os valores de uma lista existente sem precisar iterar)
lista3 = list((map(lambda x: x**2, lista)))


# Exemplo filter (cria uma lista executando um operador logico em todos os valores de uma lista existente sem precisar iterar)
lista4 = list(filter(lambda item: item % 2 == 0, lista))


# Exemplo para verificar se determinado valor está na lista
print(1 in lista)

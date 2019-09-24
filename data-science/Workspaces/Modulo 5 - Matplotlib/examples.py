import matplotlib.pyplot as plt
import numpy as np

# Setando valores
x = np.linspace(0, 5, 11)
y = x * x

# Exemplo orientado a objetos com figure
fig = plt.figure(figsize=(8, 3))
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# Setar gráfico com os valores e cores
axes.plot(x, y, 'r--')
axes.set_xlabel('Eixo X')
axes.set_title('Título')

# Cria duas instancias com um eixo e legendas incluídas
fig, ax = plt.subplots()
ax.plot(x, x**3, 'b--', label='X ao cubo')
ax.plot(x, x**4, 'g--', label='X à quarta')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_title('Titulo')
# Permitindo a inserção de legendas
ax.legend()

# Exemplo de multiplos graficos
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].plot(x, y, color='#ff0000', linestyle='-.')
ax[0].plot(y, x, color='#880088', linestyle='-.')
ax[0].set_title('Titulo')
ax[1].bar(y, x)
ax[1].set_title('Titulo')

# Setar limite do eixo x e eixo y
ax[0].set_xlim([0, 2])
ax[0].set_ylim([0, 10])

# Organizar gráficos
#plt.tight_layout()

plt.show()

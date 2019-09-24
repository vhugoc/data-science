import matplotlib.pyplot as plt

products = {
    'product': ['X Salada', 'X Bacon', 'Coca Cola 2L'],
    'value': [10.00, 12.00, 8.00]
}

fig = plt.figure(figsize=(8, 5))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.bar(products['product'], products['value'])
ax.set_ylabel('Preço')
ax.set_xlabel('Produto')
plt.show()

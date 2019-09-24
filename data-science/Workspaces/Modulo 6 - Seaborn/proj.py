import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

products = {
    'product': ['X Salada', 'X Bacon', 'Coca Cola 2L', 'Fanta Uva 2L', 'Fanta Uva 1L'],
    'category': ['Lanche', 'Lanche', 'Bebida', 'Bebida', 'Bebida'],
    'value': [10.00, 12.00, 8.00, 6.00, 4.00],
    'sells': [50, 10, 32, 16, 5]
}

data = pd.DataFrame(products)

# sns.pairplot(data, hue='category')
# sns.lineplot(x='product', y='sells', data=data)
sns.countplot(x='category', data=data)

plt.show()

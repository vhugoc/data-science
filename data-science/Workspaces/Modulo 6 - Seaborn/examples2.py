import matplotlib.pyplot as plt
import seaborn as sns

flights = sns.load_dataset('flights')
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')

# Reorganização de dados
pf = flights.pivot_table(values='passengers', index='month', columns='year')

# sns.heatmap(pf, cmap='coolwarm', linecolor='white', linewidths=1)

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='magma', markers=['o', 'v'])

plt.show()

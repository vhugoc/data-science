import matplotlib.pyplot as plt
import seaborn as sns

# Carregando um dataframe automaticamente
tips = sns.load_dataset('tips')

# Principais Plots
# sns.distplot(tips['total_bill'], kde=False)
# sns.pairplot(tips, hue="smoker")
sns.barplot(x='sex', y='total_bill', data=tips)
# sns.countplot(x='sex', data=tips)
# sns.stripplot(x='day', y='total_bill', data=tips, hue='sex', dodge=True)
# sns.violinplot(x='day', y='total_bill', data=tips, palette='rainbow')
# sns.swarmplot(x='day', y='total_bill', data=tips, color='black')
# sns.lineplot(x='day', y='total_bill', data=tips, hue='sex')

plt.show()

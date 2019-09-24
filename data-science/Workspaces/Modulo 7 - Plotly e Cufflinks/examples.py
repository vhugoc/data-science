import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#import cufflinks as cf

init_notebook_mode(connected=True)
#cf.go_offline()

df = pd.DataFrame(np.random.rand(100, 4), columns='A B C D'.split())
df2 = pd.DataFrame({
    'Categoria': ['A', 'B', 'C'],
    'Valores': [32, 43, 50]
})

df.iplot(kind='scatter', x='A', y='B', mode='markers')

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('vendas.xlsx', sheet_name='Planilha1')

df['timestamp'] = pd.to_datetime(df['Data'])

group_date = df.groupby('timestamp')
group_client = df.groupby('Cliente')

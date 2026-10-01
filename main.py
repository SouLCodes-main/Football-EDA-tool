import pandas as pd

df = pd.read_csv('data.csv')
df = df.filter(items=['Poss', 'GF'])

print(df.head())
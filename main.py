import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

df = pd.read_csv('data.csv')
df = df[['Poss', 'GF']].apply(pd.to_numeric, errors='coerce').dropna()
#df = df.filter(items=['Poss', 'GF'])
m, c =np.polyfit(df['Poss'], df['GF'], 1)
y_pred = m*df['Poss'] + c

ax.scatter(df['Poss'], df['GF'], marker='o', linestyle='-', color='b')
ax.plot(df['Poss'], y_pred, color='r', label='Expected Goals vs Possession')
ax.set_xlabel('Possession')
ax.set_ylabel('Goals Scored')
ax.set_title('Possession vs Goals Scored')
ax.legend()

plt.show()

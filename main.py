import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

df = pd.read_csv('data.csv')
df = df.filter(items=['Poss', 'GF'])
m, c =np.polyfit(df['Poss'], df['GF'], 1)

ax.scatter(df['Poss'], df['GF'], marker='o', linestyle='-', color='b')
ax.plot(df['Poss'], m*df['Poss'] + c, color='r', label='Best Fit Line')
ax.set_xlabel('Possession')
ax.set_ylabel('Goals Scored')
ax.set_title('Possession vs Goals Scored')
ax.legend()

plt.show()

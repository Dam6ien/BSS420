import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_water = pd.read_csv('runs/run_1_water.csv')
conservative = pd.read_csv('runs/run_4_water.csv')
overflow = pd.read_csv('runs/run_5_water.csv')

df1 = base_water[' renewableQuantity']
df2 = conservative[' renewableQuantity']
df3 = overflow[' renewableQuantity']

new_df = pd.DataFrame()
new_df['base'] = df1.values
new_df['conservative'] = df2.values
new_df['overflow'] = df3.values

new_df.to_csv('water.csv')

'''
==============
Plots
==============
'''

rc = {
    "font.size":20,
    "axes.titlesize":25,
    "axes.labelsize":18,
    "figure.figsize": (15,10)
}
sns.set(rc=rc)

ax = sns.distplot(base_water[' renewableQuantity'], label='Base model', color='#ffffff', kde = False)
sns.distplot(conservative[' renewableQuantity'], label='Conservative', color='#C1C1C1', kde = False)
sns.distplot(overflow[' renewableQuantity'], label='Overflow', color='#333333', kde = False)

ax.set(xlabel='Water quantity (litres)', ylabel='Frequency', title='Reusable water collected ')
plt.legend()
plt.show()
plt.savefig("example.png") 
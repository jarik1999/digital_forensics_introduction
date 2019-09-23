import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd

# hide diagram
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

# column names
columns = ['Top Sellers', 'Rating', 'Orders Complete', 'Trusted?', 'Level']

# read excel document
data = pd.read_excel('sellers.xlsx')
df = pd.DataFrame(data, columns = columns)
entries = df.values

# Create the table
ax.table(cellText = entries, colLabels=columns, loc = 'center')

fig.tight_layout()
plt.show()
import pandas as pd
import xlrd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# read seller columns from excel document
data = pd.read_excel('sample.xlsx')
df = pd.DataFrame(data, columns = ['Seller'])

# get top 10 sellers
top10 = df['Seller'].value_counts().head(10)

# get names & values
xNames = top10.keys()
positions = np.arange(len(xNames))
yValues = top10.tolist()

# create bar diagram
plt.bar(positions, yValues, align = 'center', alpha = 0.5)
plt.xticks(positions, xNames)
plt.ylabel('Products')
plt.title('Top Sellers')
plt.show()



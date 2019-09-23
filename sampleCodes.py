import pandas as pd
import xlrd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# read excel document with certain columns
data = pd.read_excel('sample.xlsx')
df = pd.DataFrame(data, columns = ['Seller', 'Item', 'Details'])

# get list of sellers to get most popular
sellers = df['Seller'].value_counts()
# get array of entries
entries = df.values
# get top 3 sellers
top3 = df['Seller'].value_counts().head(3)

xNames = ('a', 'b', 'c')
positions = np.arange(len(xNames))
yValues = [4, 1, 1]

plt.bar(positions, yValues, align = 'center', alpha = 0.5)
plt.xticks(positions, xNames)
plt.ylabel('Products')
plt.title('Top Sellers')
plt.show()



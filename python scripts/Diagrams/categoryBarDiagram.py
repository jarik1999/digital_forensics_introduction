import pandas as pd
import xlrd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# read seller columns from excel document
data = pd.read_excel('sample.xlsx')
df = pd.DataFrame(data, columns = ['Category'])

# get top 10 sellers
categories = df['Category'].value_counts()

# get names & values
xCategories = categories.keys()
positions = np.arange(len(xCategories))
yValues = categories.tolist()

# create bar diagram
plt.bar(positions, yValues, align = 'center', alpha = 1)
plt.xticks(positions, xCategories)
plt.ylabel('Posts')
plt.title('Categories')
plt.show()
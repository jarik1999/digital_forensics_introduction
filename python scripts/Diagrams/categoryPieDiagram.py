import pandas as pd
import xlrd
import matplotlib.pyplot as plt

# read seller columns from excel document
data = pd.read_excel('sample.xlsx')
df = pd.DataFrame(data, columns = ['Category'])

# get categories & sizes
values = df['Category'].value_counts()
categories = values.keys()
sizes = values.tolist()

# create pie diagram
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels = categories, autopct = '%1.1f%%', shadow = True, startangle = 90)
ax1.axis('equal')
plt.show()

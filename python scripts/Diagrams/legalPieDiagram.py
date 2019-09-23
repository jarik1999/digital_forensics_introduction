import pandas as pd
import xlrd
import matplotlib.pyplot as plt

# read seller columns from excel document
data = pd.read_excel('sample.xlsx')
df = pd.DataFrame(data, columns = ['Legal'])

# count legal/illegal
entries = df.values
yes = 0
no = 0
for entry in entries:
	if entry[0].lower() == 'yes': yes += 1
	elif entry[0].lower() == 'no': no += 1
	else: raise Exception(entry[0].lower())

# get names & wieghts for diagram
weights = [yes, no]
names = ['legal', 'illegal']

# create pie diagram
fig1, ax1 = plt.subplots()
ax1.pie(weights, labels = names, autopct = '%1.1f%%', shadow = True, startangle = 90)
ax1.axis('equal')
plt.show()

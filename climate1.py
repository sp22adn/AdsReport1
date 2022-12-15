 
#Importing the  library packages required

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

# Read Excel file and check statistics

data = pd.read_csv("D:\Datasets\dataforcountry.csv")

#Printing the data

data.head(5)

# Index to be set as Country/Region

data=data.set_index('Country/Region')

# Printing the transpose form of new dataframe

data.T.head(5)

# ploting of the mean value

X=data.mean().plot() 
plt.figure()
plt.hist(data['1998'], bins= 77);

# ploting heatmap for five regions of the world

plt.title('visualization');
sn.heatmap(data.isnull())

# countploting for the year 2000

sn.countplot('2000', data=data, palette='Set3')
plt.show()

# Visualization of the data from the year 1990 to 2019

ns = list(data.select_dtypes(['float64', 'int64']).keys())
data[ns].hist(figsize=(20,10), color='purple', edgecolor='white')
plt.show()

# Regplot of the year 1998 and 2000

sn.regplot(x='1998', y='2000', data=data, color='g')
plt.show()



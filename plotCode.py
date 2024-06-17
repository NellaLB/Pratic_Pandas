import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data.csv')
pd.DataFrame(data)

#Convert dataframe to array
array = data.to_numpy()
print(array)
print(data.corr())

#Creation of plot
data.plot(kind='scatter',x='Calories',y='Duration').get_figure().savefig('plot.png')
plt.show()
import pandas as pd

#Get CSV file
dataframe = pd.read_csv('listeEnfants.csv')
pd.DataFrame(dataframe)

#Cleaning data
for row in dataframe.index:
    serie = list(dataframe.iloc[row])
    for nbCol in range(len(serie)):
        if serie[nbCol].isnumeric():
            serie[nbCol]=None
            dataframe.loc[row] = pd.Series(serie)
dataframe.drop_duplicates(inplace=True)
dataframe.dropna(inplace = True)
dataframe.reset_index(inplace = True, drop = True)

#Show data (tables)
print(dataframe.to_string())
import pandas as pd

#Get CSV file
dataframe = pd.read_csv('listeEnfants.csv')
pd.DataFrame(dataframe)

#Cleaning data
for row in dataframe.index:
    serie = list(dataframe.loc[row])
    for nbCol in range(len(serie)):
        if serie[nbCol].strip().isnumeric() or serie[nbCol] == " ":
            dataframe.drop(labels=row, inplace = True)
dataframe.drop_duplicates(inplace=True)
dataframe.dropna(inplace = True)
dataframe.reset_index(inplace = True, drop = True)

#Show data (tables)
print(dataframe.to_string())
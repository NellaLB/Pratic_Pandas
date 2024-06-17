import pandas as pd

#Get CSV file
dataframe = pd.read_csv('listeEnfants.csv')
pd.DataFrame(dataframe)

#Cleaning data
for row in dataframe.index:
    if not(dataframe.loc[row,'Nom'].isalpha()):
        dataframe.loc[row,'Nom'] = None
dataframe.drop_duplicates(inplace=True)
dataframe.dropna(inplace = True)
dataframe.reset_index(inplace = True, drop = True)

#Show data (tables)
print(dataframe.to_string())

#Choose to print one item
row , column = input("Donnez une ligne et colonne séparée par une virgule :   ").split(",")
row = int(row.strip())
print(dataframe.iloc[row][column.strip()])

#Turn into CSV file
dataframe.to_csv('listeEnfantsCorr.csv',
    sep=',',
    header=True,
    index=False,
    encoding='utf-8'
)
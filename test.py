import pandas as pd

#Get CSV file
dataframe = pd.read_csv('listeEnfants.csv')
pd.DataFrame(dataframe)

#Cleaning data
for column in dataframe.columns:
    serie = dataframe[column]
    for nbRow in range(serie.size):
        try:
            serie[nbRow].astype(int)
            serie[nbRow]=None
            dataframe[column] = serie
        except:
            pass
dataframe.drop_duplicates(inplace=True)
dataframe.dropna(inplace = True)
dataframe.reset_index(inplace = True, drop = True)

#Show data (tables)
print(dataframe.to_string())
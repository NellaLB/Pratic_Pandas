import pandas as pd
import numpy as np

array1 = np.array([[3,4],[3,9]])

dataframe1 = pd.DataFrame(array1)

print(dataframe1.to_string())
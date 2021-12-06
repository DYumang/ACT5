import pandas as pd
data = pd.read_csv('Apr28_2021.csv')
print(data.isna().sum())
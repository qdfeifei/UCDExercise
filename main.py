
#main py pushed to Github for week3

import pandas
df=pandas.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")
print(df.describe())
print(df.head())

df2=pandas.read_csv("titanic.csv")
print(df2.describe())
print(df2.head())
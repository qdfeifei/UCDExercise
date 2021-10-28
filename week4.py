# week4 working with csv
import pandas as pd
netflix_data= pd.read_csv("netflix_titles.csv")
print(netflix_data.head())
print(netflix_data.shape)

#pring missing value
missing_values_count = netflix_data.isnull().sum()
print(missing_values_count[0:12])

#drop rows and columns
#droprows= netflix_data.dropna(axis=1)
#print(netflix_data.shape,droprows.shape)
#dropcolumns = netflix_data.dropna(axis=1)
#print(netflix_data.shape,dropcolumns.shape)

#filled with 0
#cleaned_data = netflix_data.fillna(0)
#cleaned_data = netflix_data.fillna(method='bfill', axis=0).fillna(0)
#print(cleaned_data.shape)

#drop the duplicated
drop_duplicates= netflix_data.drop_duplicates()
print(netflix_data.shape,drop_duplicates.shape)

drop_duplicates= netflix_data.drop_duplicates(subset=['type'])
print(netflix_data.shape,drop_duplicates.shape)
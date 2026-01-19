import pandas as pd

raw_data=pd.read_csv("F:/house-prices-advanced-regression-techniques/test.csv")

# print(raw_data.shape)
print("Total missing BEFORE:", raw_data.isna().sum().sum())
#Indexing status of missing values
missing_values= raw_data.isnull().sum()

#Threshold
threshold= 0.75 * len(raw_data)

#Separating two levels of missing value
less = missing_values[missing_values <= threshold].index
over = missing_values[missing_values > threshold].index


#Cleaning in Numeric Data
numeric_features= raw_data[less].select_dtypes(include=['number']).columns
raw_data[numeric_features] = raw_data[numeric_features].fillna(raw_data[numeric_features].median)

#Cleaning Categorical Data
categorical_features= raw_data[less].select_dtypes(include=["object"]).columns
for column in categorical_features:
    raw_data[column]= raw_data[column].fillna(raw_data[column].mode()[0])

#Finishing dengan menghapus over missing values
clean_data=raw_data.drop(columns=over)

print("Total missing AFTER :", clean_data.isna().sum().sum())

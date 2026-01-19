import pandas as pd

#loading dataset -> csv
train=pd.read_csv("F:/house-prices-advanced-regression-techniques/train.csv")
# train.info()
# print(train.describe(include="all"))


#MENGATASI MISSING VALUES
missing_values = train.isnull().sum()
less = missing_values[missing_values < 1000].index
over = missing_values[missing_values >= 1000].index


#MISSING VALUES DI TIPE DATA NUMERIK
#Mengambil feature yg punya tipe data number
numeric_data= train[less].select_dtypes(include=['number']).columns

#Mengisi missing values dengan median(Nilai Tengah)
train[numeric_data]=train[numeric_data].fillna(train[numeric_data].median())


#MISSING VALUES DI TIPE DATA KATEGORIKAL
kategorical_features = train[less].select_dtypes(include=['object']).columns
 
for column in kategorical_features:
    train[column] = train[column].fillna(train[column].mode()[0])

x=train.isna().sum().sort_values(ascending=False).head(20)
print(x)

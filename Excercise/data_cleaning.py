import pandas as pd

#loading dataset -> csv
dirty_data=pd.read_csv("F:/house-prices-advanced-regression-techniques/train.csv")
# train.info()
# print(train.describe(include="all"))


#MENGATASI MISSING VALUES
missing_values = dirty_data.isnull().sum()
less = missing_values[missing_values < 1000].index
over = missing_values[missing_values >= 1000].index


#MISSING VALUES DI TIPE DATA NUMERIK
#Mengambil feature yg punya tipe data number
numeric_data= dirty_data[less].select_dtypes(include=['number']).columns

#Mengisi missing values dengan median(Nilai Tengah)
dirty_data[numeric_data]=dirty_data[numeric_data].fillna(dirty_data[numeric_data].median())


#MISSING VALUES DI TIPE DATA KATEGORIKAL
kategorical_features = dirty_data[less].select_dtypes(include=['object']).columns

#Isi missing values kategorikal dengan modus (nilai yang paling sering muncul)
for column in kategorical_features:
    dirty_data[column] = dirty_data[column].fillna(dirty_data[column].mode()[0])

# #Isi missing values kategorikal dengan string "missing"
# for miss in kategorical_features:
#     train[miss] = train[miss].fillna("missing")


#Menghapus over missing values
clean_data= dirty_data.drop(columns=over)


# #Check Apakah masih ada missing values atau tidak.
# x=clean_data.isna().sum().sort_values(ascending=False).head(20)
# print(x)
# missing_values = clean_data.isnull().sum()
# print(missing_values[missing_values > 0])
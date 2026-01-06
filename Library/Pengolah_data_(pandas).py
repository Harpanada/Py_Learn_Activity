import pandas as pd
from datetime import date

data={
    'Name': ['Toyaa','Christy','Cathleen','Nixie'],
    'Date of Birth': [date(2005,12,5), date(2005,11,20), date(2009,5,28), date(2009,5,13)],
    'Address': ['West Jakarta','Center Jakarta','Surabaya','South Jakarta'],
}

def hitungUmur(dtof_birth):
    today= date.today()
    age= today.year-dtof_birth.year
    if (today.month, today.day) < (dtof_birth.month, dtof_birth.day):
        age -= 1
    return age

ages=[]
for dtof_birth in data['Date of Birth']:
    ages.append(hitungUmur(dtof_birth))

data_final = {
    'Name': data['Name'],
    'Age': ages,
    'Date of Birth': data['Date of Birth'],
    'Address': data['Address'],
}


#Example of Use Pandas as table/data frame maker
data_frame=pd.DataFrame(data_final)
print(data_frame)
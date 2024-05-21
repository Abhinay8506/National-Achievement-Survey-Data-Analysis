import pandas as pd
from matplotlib import pyplot as plt
import os

#Setting dataset absolute path
os.chdir(r"C:\Users\user\Downloads")

#Reading Dataset
st=pd.read_csv("surveydataset.csv")

#Checking shape means (No. of rows,No. of columns)
st.shape

#First 5 rows
st.head()

#Maximum no. of columns to observe
pd.set_option('display.max_columns', None)
st

#State counts
st['State'].value_counts()

#District counts
st['District'].value_counts()

#Classes count
st['Class'].value_counts()

#No. of schools
st['Number of schools surveyed'].value_counts()

#Year surveyed
st['Year'].value_counts()

#First 10 records of !2017
info1=st[st['YearCode']!=2017]
info1.head(10)

#First 10 records of !2021
info2=st[st['YearCode']!=2021]
info2.head(10)



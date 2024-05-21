import pandas as pd
from matplotlib import pyplot as plt
import os

#Setting dataset absolute path
os.chdir(r"C:\Users\user\Downloads")

#Reading Dataset
st=pd.read_csv("surveydataset.csv")


#making a bar plot of states.
plt.figure(figsize=(15,5))
plt.bar(list(st['State'].value_counts()[:10].keys()),list(st['State'].value_counts()[:10]),color='g')
plt.show()



#making a bar plot of states.
plt.figure(figsize=(15,5))
plt.bar(list(st['State'].value_counts()[:10].keys()),list(st['State'].value_counts()[:10]),color='g')
plt.show()

# Filter out rows where 'YearCode' is not equal to 2017
filtered_st = st[st['YearCode'] != 2017]

# Take the top 10 states by count
top_states = filtered_st['State'].value_counts().head(10)

# Plotting
plt.figure(figsize=(15, 5))
plt.bar(top_states.index, top_states.values, color='r')
plt.xlabel('State')
plt.ylabel('Count')
plt.title('Top 10 States by Count')
plt.show()



# Filter out rows where 'YearCode' is not equal to 2021
filtered_st = st[st['YearCode'] != 2021]

# Take the top 10 states by count
top_states1 = filtered_st['District'].value_counts().head(10)
top_states2 = filtered_st['Number of schools surveyed'].value_counts().head(10)

# Plotting- no. of school in 
plt.figure(figsize=(15, 5))
plt.bar(top_states1.index, top_states2.index, color='b')
plt.xlabel('District')
plt.ylabel('Number of schools surveyed')
plt.title('Top 10 States by Count 2017')
plt.show()



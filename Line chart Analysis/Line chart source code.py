import pandas as pd
from matplotlib import pyplot as plt
import os

#Setting dataset absolute path
os.chdir(r"C:\Users\user\Downloads")

#Reading Dataset
st=pd.read_csv("surveydataset.csv")

# Filter out rows where 'YearCode' is not equal to 2021
filtered_st = st[st['YearCode'] !=2021]
# Define the columns which we want to compare
x_column =  'District'   
y_column =  'Number of schools surveyed'
   
# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()


# Filter out rows where 'YearCode' is not equal to 2017
filtered_st = st[st['YearCode'] !=2017]

# Define the columns which we want to compare
x_column =  'District'   
y_column =  'Number of schools surveyed' 

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)
# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()



# Filter out rows where 'YearCode' is not equal to 2021
filtered_st = st[st['YearCode'] !=2021]

# Define the columns which we want to compare
x_column =  'District'  
y_column =  'Number of students surveyed'  

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 8))
plt.plot(first_10_rows[x_column], first_10_rows[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()


# Filter out rows where 'YearCode' is not equal to 2017
filtered_st = st[st['YearCode'] !=2017]

# Define the columns which we want to compare
x_column =  'District'  
y_column =  'Number of students surveyed' 

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 8))
plt.plot(first_10_rows[x_column], first_10_rows[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()


# Filter out rows where 'YearCode' is not equal to 2021
filtered_st = st[st['YearCode'] !=2021]

# Define the columns which we want to compare
x_column =  'District'   
y_column =  'Average performance of students on learning outcome SST807 Social Science'  

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()


# Filter out rows where 'YearCode' is not equal to 2017
filtered_st = st[st['YearCode'] !=2017]

# Define the columns which we want to compare
x_column =  'District'   
y_column =  'Average performance of students on learning outcome SST807 Social Science'  

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()


# Filter out rows where 'YearCode' is not equal to 2021
filtered_st = st[st['YearCode'] !=2021]

# Define the columns you want to compare
x_column =  'District'  # Replace 'X_Column' with the name of the x-axis column
y_column =  'Average performance of students on learning outcome SST810 Social Science' # Replace 'Y_Column' with the name of the y-axis column

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()


# Filter out rows where 'YearCode' is not equal to 2017
filtered_st = st[st['YearCode'] !=2017]

 # Define the columns which we want to compare
x_column =  'District'  
y_column =  'Average performance of students on learning outcome SST810 Social Science'  

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()


# Filter out rows where 'YearCode' is not equal to 2021
filtered_st = st[st['YearCode'] !=2021]

# Define the columns which we want to compare
x_column =  'District'   
y_column =  'Average performance of students on learning outcome M601 Mathematics'  

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()


# Filter out rows where 'YearCode' is not equal to 2017
filtered_st = st[st['YearCode'] !=2017]

# Define the columns which we want to compare
x_column =  'District'   
y_column =  'Average performance of students on learning outcome M601 Mathematics'  

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()


# Filter out rows where 'YearCode' is not equal to 2021
filtered_st = st[st['YearCode'] !=2021]

# Define the columns which we want to compare
x_column =  'District'   
y_column =  'Average performance of students on learning outcome M606 Mathematics'  

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()


# Filter out rows where 'YearCode' is not equal to 2017
filtered_st = st[st['YearCode'] !=2017]

# Define the columns which we want to compare
x_column =  'District'   
y_column =  'Average performance of students on learning outcome M606 Mathematics'  

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()




# Filter out rows where 'YearCode' is not equal to 2021
filtered_st = st[st['YearCode'] !=2021]

# Define the columns which we want to compare
x_column =  'District'   
y_column =  'Average performance of students on learning outcome SCI703 Science'  

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column],color='yellow')
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()







# Filter out rows where 'YearCode' is not equal to 2017
filtered_st = st[st['YearCode'] !=2017]

# Define the columns which we want to compare
x_column =  'District'   
y_column =  'Average performance of students on learning outcome SCI703 Science' 

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column],color='orange')
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()



# Filter out rows where 'YearCode' is not equal to 2021
filtered_st = st[st['YearCode'] !=2021]

# Define the columns which we want to compare
x_column =  'District'  
y_column =  'Average performance of students on learning outcome SCI704 Science'  

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()


# Filter out rows where 'YearCode' is not equal to 2017
filtered_st = st[st['YearCode'] !=2017]

# Define the columns which we want to compare
x_column =  'District'  
y_column =  'Average performance of students on learning outcome SCI704 Science' 

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column],color='black')
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()


# Filter out rows where 'YearCode' is not equal to 2021
filtered_st = st[st['YearCode'] !=2021]

# Define the columns which we want to compare
x_column =  'District'   
y_column =  'Average performance of students on learning outcome L813 Language' 

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column],color='green')
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()



# Filter out rows where 'YearCode' is not equal to 2017
filtered_st = st[st['YearCode'] !=2017]

# Define the columns which we want to compare
x_column =  'District'   
y_column =  'Average performance of students on learning outcome L813 Language'  

# Select the first 10 rows of the DataFrame
first_10_rows = filtered_st.head(10)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(first_10_rows[x_column], first_10_rows[y_column],color='red')
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title('Plot of {} vs {}'.format(y_column, x_column))
plt.grid(True)
plt.show()


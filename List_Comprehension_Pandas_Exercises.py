# List Comprehension and Pandas Exercises
# Author: Nesibe Seyma CAN
# Description: Practice exercises covering Python list comprehensions and basic Pandas operations.

# Task 1:
# Using a list comprehension, convert the names of the numeric variables
# in the car_crashes dataset to uppercase and add the prefix 'NUM'.

#The names of the non-numeric variables should also be converted to uppercase. A single list comprehension must be used.

import seaborn as sns
df=sns.load_dataset('car_crashes')
df.columns
df.head()
["NUM"+ col_name.upper() if df[col_name].dtype != "O" else col_name.upper() for col_name in df.columns ]

# Task 2:
# Using a list comprehension, add the suffix 'FLAG' to the names of the variables
# in the car_crashes dataset that do not contain the string 'no'.

[col+"FLAG" if "no" not in col.lower() else col for col in df.columns ]

# Task 3:
# Using a list comprehension, select the variable names that are different from
# the ones given below and create a new DataFrame.

og_list  = ["abbrev", "no_previous"]

#First, create a new list named new_cols based on the given list using a list comprehension.
#Then, select these variables with df[new_cols] and create a new DataFrame named new_df "

new_cols=[col_name for col_name in df.columns if col_name not in og_list ]
new_df = df[new_cols]
new_df.head()

# Task 1: Load the Titanic dataset from the Seaborn library.
import seaborn as sns
df2= sns.load_dataset("titanic")
# Task 2: Find the number of female and male passengers in the Titanic dataset.
df2["sex"].value_counts()
# Task 3: Find the number of unique values for each column.
df2.nunique()
# Task 4: Find unique values in the "pclass" variable.
df2.pclass.unique()
# Task 5: Find the number of unique values in the "pclass" and "parch" variables.
df2[["pclass","parch"]].nunique()
# Task 6: Check the data type of the "embarked" variable. Change its type to "category" and check again.
df2["embarked"].dtype
df2["embarked"]=df2["embarked"].astype("category")
# Task 7: Display all information of the passengers whose "embarked" value is "C".
df2.loc[df2["embarked"]=="C", :]
import pandas as pd
pd.set_option('display.max_columns', None) #I changed the display options to see embarked values.
# Task 8: Display all information of the passengers whose "embarked" value is not "S".
df2.loc[df2["embarked"]!="S", :]
# Task 9: Display all information of the passengers who are female and younger than 30.
df2[(df2["sex"]== "female") & (df2["age"]<30) ].head()
# Task 10: Display all information of the passengers whose fare is greater than 500 or whose age is greater than 70.
df2[(df2["fare"]> 500) | (df2["age"] >70) ].head()
# Task 11: Find the total number of missing values in each variable.
df2.isnull().sum()
# Task 12: Drop the "who" variable from the DataFrame.
df2.drop("who", axis=1 , inplace=True)
df2.columns
# Task 13: Fill the missing values in the "deck" variable with the most frequent value (mode) of "deck".
df2.deck.mode()
type(df2.deck.mode()) #pandas.series .so cann not fill the missing values
df2["deck"] = df2["deck"].fillna(df2["deck"].mode()[0])
df2.deck.isnull().any()
# Task 14: Fill the missing values in the "age" variable with the median of "age".
df2["age"]=df2["age"].fillna(df2["age"].median())
df2.age.isnull().any()
# Task 15: Find the sum, count, and mean of the "survived" variable grouped by "pclass" and "sex".
df2.groupby(["pclass","sex"]).agg({ "survived" : ["sum","count","mean"]})
# Task 16: Write a function that assigns 1 to passengers younger than 30, and 0 to passengers 30 and older.
# Using this function, create a new variable called "age_flag" in the Titanic dataset (use apply and lambda).
df2["age_flag"]=df2["age"].apply(lambda x : 1 if x<30 else 0)
pd.set_option('display.width', 500)
df2.head()



# Task 17: Load the Tips dataset from the Seaborn library.
df3=sns.load_dataset("tips")
# Task 18: Find the sum, min, max, and mean of total_bill values by the categories of the Time variable (Dinner, Lunch).
df3.groupby("time").agg({"total_bill": ["sum","min","max","mean"]})
# Task 19: Find the sum, min, max, and mean of total_bill values by days and time.
df3.groupby(["day","time"]).agg({"total_bill": ["sum","min","max","mean"]})
# Task 20: For Lunch time and female customers, find the sum, min, max, and mean of total_bill and tip values by day.
df3[(df3["sex"]== "Female")&(df3["time"]== "Lunch")].groupby("day").agg({"total_bill": ["sum","min","max","mean"],
                                                                      "tip":["sum","min","max","mean"]})
# Task 21: What is the average of orders with size less than 3 and total_bill greater than 10? (use loc)
df3.loc[(df3["size"]<3)&(df3["total_bill"]>10),"total_bill"].mean()
# Task 22: Create a new variable named total_bill_tip_sum.
# It should represent the sum of total_bill and tip paid by each customer.
df3["total_bill_tip_sum"]=df3["total_bill"]+df3["tip"]
df3.head()
# Task 23: Sort the total_bill_tip_sum variable in descending order and assign the first 30 customers to a new dataframe.
new_df=df3.sort_values("total_bill_tip_sum",ascending=False)[:30]
new_df.head()
new_df.shape
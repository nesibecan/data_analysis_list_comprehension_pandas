#Rule-based classification for predicting potential customer profitability
#AUTHOR: NESIBE SEYMA CAN

import pandas as pd
pd.set_option("display.max_columns", None)
df = pd.read_excel('Rule-based classification for predicting potential customer profitability/miuul_gezinomi.xlsx')
pd.set_option('display.float_format', lambda x: '%.2f' % x)
print(df.head())
print(df.shape)
print(df.info())

#Number of unique cities and their frequency counts.

print(df["SaleCityName"].nunique())
print(df["SaleCityName"].value_counts())

#Number of distinct hotel concepts and the frequency of sales for each concept.
df["ConceptName"].nunique()
df["ConceptName"].value_counts()

#Total sales revenue by city and by concept.
df.groupby("SaleCityName").agg({"Price": "sum"})
df.groupby("ConceptName").agg({"Price": "sum"})

#Average sales price per city.
df.groupby(by=['SaleCityName']).agg({"Price": "mean"})
#Average sales price per hotel concept.
df.groupby(by=['ConceptName']).agg({"Price": "mean"})

#Average sales prices by city–concept breakdown
df.groupby(by=["SaleCityName", 'ConceptName']).agg({"Price": "mean"})

#Task 2: Transform satis_checkin_day_diff into a categorical variable named EB_Score.
#
bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)
df.head(50).to_excel("eb_scorew.xlsx", index=False)

#Average Prices and Frequencies by City, Concept, EB_Score, Season, and CInDay.

df.groupby(by=["SaleCityName", 'ConceptName', "EB_Score" ]).agg({"Price": ["mean", "count"]})

df.groupby(by=["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean", "count"]})

df.groupby(by=["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean", "count"]})

#Sort the City–Concept–Season breakdown by PRICE (descending) and save as agg_df. ✅

agg_df = (df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values
          ("Price", ascending=False))
agg_df.head(20)

#Convert index names to columns
agg_df.reset_index(inplace=True)
agg_df.head()

#Defining the sales_level_based variable and add it to the dataframe. ✅
agg_df['sales_level_based'] = (agg_df[["SaleCityName", "ConceptName", "Seasons"]]
                               .agg(lambda x: '_'.join(x).upper(), axis=1))

agg_df.head()

#Segment personas by PRICE.
agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})

# Business Task:
# Sort the final dataframe by PRICE and identify the segment and expected price for “ANTALYA_HERŞEY DAHIL_HIGH”. ✅

agg_df.sort_values(by="Price")

new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
agg_df[agg_df["sales_level_based"] == new_user]


# Loading data from the files using sqllite and pandas,
# Cleaning the data and transforming it,
# Creating multiple analysis KPI's such as churn rate, revenue loss, churn by state, customer life time value and many other.



# import lib

import sqlite3

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

# 1. import database

conn = sqlite3.connect("../data/customer_churn.db")

sql_query = """
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'

"""
tables = pd.read_sql(sql_query, conn)

# create dataframe for each table
df = {}
for table_name in tables["name"]:
    df[f"df_{table_name}"] = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    print(f"Created dataframe: df_{table_name}")

conn.close()

# print table name and column names
conn = sqlite3.connect("../data/customer_churn.db")

for table_name in tables["name"]:
    print(f"\nTable Name: {table_name}")
    # get column information
    columns_query = f"PRAGMA table_info({table_name});"
    columns = pd.read_sql(columns_query, conn)
    print("Columns:")
    print(columns["name"].tolist())

conn.close()

# 2. data cleaning

df["df_db_customer"].head()
df["df_db_customer"].tail()
df["df_db_customer"].info()

# rename col - name

df["df_db_customer"] = df["df_db_customer"].rename(columns={"name": "customer_name"})

# drop columns interest and pincode

# df["df_db_customer"] =  df['df_db_customer'].drop(columns = df['df_db_customer'].columns[-2:])
df["df_db_customer"] = df["df_db_customer"].drop(columns=["interests", "pincode"])

# change data type - dob

df["df_db_customer"]["dob"] = pd.to_datetime(df["df_db_customer"]["dob"])

# data standardization - gender

df["df_db_customer"]["gender"].unique()
df["df_db_customer"]["gender"] = (
    df["df_db_customer"]["gender"]
    .str.strip()
    .str.lower()
    .replace({"men": "Male", "women": "Female"})
    .str.title()
)

# fix missing values - county

df["df_db_customer"][df["df_db_customer"]["country"].isna()]
df["df_db_customer"][["country", "state"]]

state_country_mapping = df["df_db_customer"].dropna(subset=["country"]).set_index("state")["country"].to_dict()

df["df_db_customer"]["country"] = df["df_db_customer"]["country"].fillna(df["df_db_customer"]["state"].map(state_country_mapping))


## subscription table

df["df_db_subscription"].head()
df["df_db_subscription"].info()

date_col= ["subscription_start_date", "renewal_date", "cancellation_date"]

df["df_db_subscription"][date_col] = df["df_db_subscription"][date_col].apply(pd.to_datetime)

df["df_db_subscription"].info()

# third table

df["df_db_support"].info()
df["df_db_support"] = df["df_db_support"].drop(columns = ['col_1', 'comment'])

df["df_db_support"]["complaint_date"] = pd.to_datetime(df["df_db_support"]["complaint_date"])


# feature engineering and data analysis and fixing table 3 due to duplicate record

df["df_db_subscription"]["churn_flag"] = np.where(df["df_db_subscription"]["cancellation_date"].notna(), 1, 0)

df["df_db_subscription"].head()

df["df_db_support"]['complaint_count'] = df["df_db_support"].groupby('customerid')['customerid'].transform('count')
df["df_db_support"] = df["df_db_support"].sort_values('complaint_date').drop_duplicates('customerid', keep = 'last')

df1 = df["df_db_subscription"].merge(df["df_db_customer"], on = 'customerid', how = 'left').merge(df["df_db_support"], on = 'customerid', how = 'left')

df1.to_csv('exported_churn_data.csv', index = False)


# data analysis

#1 churn rate

df1.columns

churn_rate = round(df1['churn_flag'].mean()*100, 2)
print("churn rate = ",  churn_rate, "%")
retention_rate = 100 - churn_rate
print("retentioon rate = ",  retention_rate, "%")

#2 churn by plan type

churn_by_plan = df1.groupby('plan_type')['churn_flag'].mean().round(2).mul(100).reset_index(name = 'churn_rate_pct')
print(churn_by_plan)

# 3 arpu avg revenue per user
arpu = df1['monthly_charges'].mean().round(2)
print(arpu)

# avg customer tenue
# count of days user has used our service : cancellation date else current date
today = pd.Timestamp.today()

df1['tenure_days'] = np.where(
    df1['cancellation_date'].notna(), 
    (df1['cancellation_date'] - df1['subscription_start_date']).dt.days, 
    (today - df1['subscription_start_date']).dt.days
)
avg_tenure = df1['tenure_days'].mean().round(0)
print("avg tenure days ", avg_tenure)

# revenue at risk - revenue lost from churned users

revenue_at_risk = df1.loc[df1['churn_flag']==1, 'monthly_charges'].sum()*100/ df1['monthly_charges'].sum() 

print("revenue loss = ", round(revenue_at_risk, 2), "%")

# escalation rate

escalation_rate = (df1['escalations']== 'Y').mean().round(4)*100
print(escalation_rate)

# avg complaint per user

avg_complaints = df1['complaint_count'].sum()/df1['customerid'].nunique()


print("avg complaints = ", round(avg_complaints, 2))

# correlation escalation vs churn

df1['escalations'] =  np.where(df1['escalations']=='Y', 1, 0)
corr_df = df1[['escalations', 'churn_flag']].dropna()
correlation = corr_df['escalations'].corr(df1['churn_flag'])
print("correlation between escalation vs churn is = ", round(correlation, 2))

# churn risk - create a column using exisiting col
conditions = [
    (df1['churn_score'] < 50),
    (df1['churn_score'] >= 50) & (df1['churn_score'] < 70),
    (df1['churn_score'] >= 70),
]
choices = ['low', 'med', 'high']
df1['churn_risk'] = np.select(conditions, choices, default = 'unknown')
print(df1['churn_risk'])


 # Saving the data in original df 
df = df1 
df.head()


# customer life time value
avg_cltv = (df['monthly_charges']* (df['tenure_days']/30)).mean()
print("Average customer life time value is ", round(avg_cltv, 2))

# churn by state

churn_by_state = df.groupby('state')['churn_flag'].mean()*100
print("churn rate by state", churn_by_state)
# visualization using matplotlib

df_visual = df.copy()

# monthly churn trend time series

df_visual['cancellation_month'] = df_visual['cancellation_date'].dt.to_period('M') 
churn_trend = df_visual[df_visual['churn_flag'] == 1].groupby('cancellation_month').size()
plt.figure(figsize= (8,3))
plt.plot(churn_trend.index.astype('str'), churn_trend.values, color = 'green', marker = 'o', linestyle = 'dashed', linewidth = 2, markersize = 12)
plt.title('Monthly Churn Trend')
plt.xlabel("month")
plt.ylabel("churned customers")
plt.show()


# churn by plan type

churn_type = df_visual.groupby('plan_type')['churn_flag'].mean()
plt.figure(figsize= (7, 3))
plt.bar(churn_type.index, churn_type.values)
plt.show()


# churn by state plan
churn_type = df_visual.groupby('state')['churn_flag'].mean()
plt.figure(figsize= (7, 5))
plt.bar(churn_type.index, churn_type.values)
plt.show()

# customer life time value



# pivot table

pd.pivot_table(
    df_visual,
    index = 'plan_type',
    values = ['monthly_charges', 'customerid', 'churn_flag'],
    aggfunc = {'monthly_charges': 'sum',
              'customerid': 'nunique',
              'churn_flag': 'mean'}
               )

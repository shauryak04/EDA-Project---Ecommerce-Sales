import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("ecommerce_sales.csv")

df["Date"]=pd.to_datetime(df["Date"])
df["Month"]=df["Date"].dt.month_name()
df["Weekday"]=df["Date"].dt.day_name()


df["Gross"]=df["Quantity"]*df["UnitPrice"]
df["NetAmount"]=df["Gross"]*(1-df["Discount"]/100)

df.head()
print(df.info())
print(df.describe())
print(df["Category"].value_counts())

df.isnull().sum()
df.duplicated().sum()

month_sales = df.groupby("Month")["NetAmount"].sum().reindex(
    ["January","February","March","April","May"]
    )

month_sales.plot(kind="bar")
plt.title("Total sales by month")
plt.ylabel("Net Amount")
plt.show()

weekday_sales=df.groupby("Weekday")["NetAmount"].sum()
weekday_sales.plot(kind="bar")
plt.title("Sales by weekday")
plt.show()

cat_sales=df.groupby("Category")["NetAmount"].sum()
cat_sales.plot(kind="bar")
plt.title("Category-wise Revenue")
plt.ylabel("Net Amount")
plt.show()


df["PaymentMode"].value_counts().plot(kind="bar")
plt.title("PAyment mode count")
plt.show()


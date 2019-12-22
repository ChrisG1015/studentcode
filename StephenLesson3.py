import pandas as pd

df = pd.read_csv("SalesJan2009.csv")
print(df['Transaction_date'].head(5))

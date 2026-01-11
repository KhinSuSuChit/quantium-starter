

import pandas as pd

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

df = pd.concat([pd.read_csv(f) for f in files])
df = df[df['product'] == 'pink morsel']
df['price'] = df['price'].str.replace('$', '').astype(float)
df['sales'] = df['price'] * df['quantity']
df = df.drop(["product", "price", "quantity"], axis=1)
df = df[['sales', 'date', 'region']]

#print(df)
df.to_csv('data/pink_morsel_data.csv', index=False)


'''
import csv
with open('data/daily_sales_data_1.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0
    for row in reader:
        if line_count == 0:
            print("sales, date, region")
            line_count += 1
        else:
            if row[0] == "pink morsel":
                sales = float(row[1][1:]) * float(row[2])
                print(f'{sales}, {row[3]}, {row[4]}')
            line_count += 1
            '''

import pandas as pd

df = pd.read_csv('data/daily_sales_data_1.csv')
df = df[df['product'] == 'pink morsel']
df['price'] = df['price'].str.replace('$', '').astype(float)
df['sales'] = df['price'] * df['quantity']
df = df.drop(["product", "price", "quantity"], axis=1)
df = df[['sales', 'date', 'region']]

#print(df)
df.to_csv('data/pink_morsel_data.csv', index=False)


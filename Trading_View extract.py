import pandas as pd

df = pd.read_excel('NSE_List.xlsx')
print(df.head())

NSE = [df['Symbol']]
print(NSE)
with open("NSE_List.txt","w") as fout:
    fout.write(str(NSE))

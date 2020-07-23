#!/usr/bin/env python
# coding: utf-8

# In[7]:


#this code writes csv to sql db

#import libraries
import pandas as pd
import sqlalchemy
from csv import writer
from csv import reader

#connection to sql db using sqlalchemy
engine=sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3308/citi_bridge')

#read current table
df = pd.read_sql_table('current_stock_data',engine)

#read csv generated by STOCKS.py
df = pd.read_csv("C:/Users/prach/spyder_workspace/output3.csv",header=None)
print(df)


#rename columns in csv file
df.rename(columns={0: 'stock_name', 1: 'NSE',2:'BSE'}, inplace=True)
#write into new csv
df.to_csv('output4.csv', index=False)
print(df)

#write the above csv to sql db 
df.to_sql(
    name='current_stock_data', # database table name
    con=engine,
    if_exists='append',
    index=False,
    chunksize=1
)


df = pd.read_sql_table('current_stock_data', engine)
print("")
print(df)


'''
nse = []
bse = []
arbitrage =[]
for i in range(len(stock_name)):
    nse.append(random.randint(1,500))
    bse.append(random.randint(1,500))

for i in range(len(stock_name)):
    arb=nse[i]-bse[i]
    arbitrage.append(arb)
print("Stocks : ",stock_name)
print("nse : ",nse)
print("bse : ",bse)
print("arbitrage : ",arbitrage)
stock_dict = {'STOCK_NAME':pd.Series(stock_name),'NSE':pd.Series(nse),'BSE':pd.Series(bse),'ARBITRAGE':pd.Series(arbitrage)}
stock_table =pd.DataFrame(stock_dict)
stock_table
stock_table[['NSE','BSE']].plot.bar()
'''


# In[5]:


#matplotlib inline


# In[6]:

'''
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=(10,6)
'''

# In[ ]:





import pandas as pd
import numpy as np
url="http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df=pd.read_csv(url,header=None)
#print(df)
headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rmp","city-mpg","highway-mpg","price"]
df.columns=headers     
'''print(df)
print(df.head(10))
print(df.tail(3))
print(df.dtypes)
print(df.describe())
print(df.describe(include='all'))
x=df['symboling']=df['symboling']+1      #increase number by 1
print(df['symboling'])
'''

#####  MIssing Value  ######
                             
print(df1.dropna(axis=0,inplace=True))     # if axis=1 gives error
df1=df1.dropna(axis=1,how='any')
print(df1)

'''
#####     Replace missing value    #########

df['normalized-losses']=pd.to_numeric(df['normalized-losses'],errors='coerce')   # errors used to ignore the errors
mean=df['normalized-losses'].mean()
df['normalized-losses'].replace(np.nan,mean)
print(df['normalized-losses'])
#print(df.dtypes)


###   Data Formatting      ######

df["city-mpg"]=235/df["city-mpg"]
df.rename(columns={"city-mpg":"city-L/100km"},inplace=True)
#print(df)

df['price']=pd.to_numeric(df['price'],errors='coerce')  
mean=df['price'].mean()
d=df.replace(np.nan,mean)
#print(d['price'].head(10))
d["price"]=d["price"].astype("int")
#print(d['price'].head(10))


#### Normalized Data #####

#print(d['length'].head(10))
#d["length"]=d["length"]/d["length"].max()
#d['length']=(d['length']-d['length'].min())/(d['length'].max()-d['length'].min())
d['length']=(d['length']-d['length'].mean())/d['length'].std()
#print(d['length'].head(10))

######  Binning    #######

binwidth= int((max(d['price'])-min(d['price']))/3)
bins=range(min(d['price']), max(d['price']),binwidth)
group_names=['Low','Medium','High']
d['price-binned']=pd.cut(d['price'],bins,labels=group_names)

print(d['fuel-type'])
print(pd.get_dummies(d['fuel-type']))

print(d)
'''

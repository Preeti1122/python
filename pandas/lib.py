import pandas as pd
url="http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df=pd.read_csv(url,header=None)
#print(df)
headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rmp","city-mpg","highway-mpg","price"]
df.columns=headers
print(df)
print(df.head(10))
print(df.tail(3))
print(df.dtypes)
print(df.describe())

print(df.T)
print(df.sort_index(axis=1, ascending=False))
print(df.sort_index(ascending=False))
print(df['symboling'])
print(df.iloc[3])
print(df.iloc[3:5,0:2])

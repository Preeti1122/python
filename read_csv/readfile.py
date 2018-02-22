
import pandas as pd

x=pd.read_csv("D:/python/read_csv/Book.csv",index_col=0)

#print(x)
x1=pd.DataFrame(data=x)
print(x1)

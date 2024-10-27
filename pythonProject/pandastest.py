import pandas as pd
from sklearn import datasets


#pandas series is a one dimensional labelld array

s1=pd.Series([1,2,3,4,5,6] )
print(s1)

s2=pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'] )
print(s2)
#key of dictionary automatically becomes index
s3=pd.Series({"key1":"value1","key2":"value2","key3":"value3"})
print(s3)


x={"label1":[1,2,3],"label2":[4,5,6],"label3":[7,8,9]}
pd.DataFrame(x).head()


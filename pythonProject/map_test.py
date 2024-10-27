li=[1,2,3,4,5]

def func(x):
    return x**x

def isEvenl(x):
    return x%2==0

print(list(map(func,li)))

print(list(map(func,filter((lambda x: x%2==0),li))))

#print(list(map(func,filter(isEvenl,li))))


def findMax(numbers):
    maxn = numbers[0]
    for i in numbers:
        if i>maxn:
             maxn=i
    print(maxn)


#findMax([10,3,6,11])

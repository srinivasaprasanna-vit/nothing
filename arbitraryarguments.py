def multiply(*b):
    result=1
    for i in b:
        result*=i
    return result
print(multiply(1,2,3,4,5,6))
print(multiply(10,20))
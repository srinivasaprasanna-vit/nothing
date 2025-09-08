import keyword
from keyword import iskeyword
tup=(10,20,30,40,50,60,70,80,80+10)
print("Tuple:",tup)
print("Accessing elements of tuple:",tup[3])
print("Slicing tuple:",tup[1:],tup[4:9])
print("len of tuple:",len(tup))
print("index:",tup.index(80))

print(iskeyword('tuple'))

num=[10,20,30,40,50]
t1= tuple(num)
print(t1)

try:
    t1.append(88)
    print(t1)
except AttributeError as e:
    print("Error:",e)
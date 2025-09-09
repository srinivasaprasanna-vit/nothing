my_dict={}
print(my_dict)

my_dict={1:"apple",2:"ball"}
print(my_dict)

print(my_dict.get(1))

d1={"name":"John", 1:[1,2,3]}
print(d1)
print(d1.get(1))


d2=dict({1:"apple",2:"ball"})
print(d2)

d3=dict([(1,"apple"),(2,"ball")])
print(d3)

x=d2.items()

print(x)

y=d2.keys()
print(y)

z=d2.values()
print(z)

d3.update({3:"cat"})
print(d2)

d2[1]="potato"
print(d2) 
L1 = []
print("Blank List: ", L1)

L2 = [10,20,14]
print("\nList of numbers: ", L2)
print("Accessing Elements of list:", L2[1])
print("Accessing the elements of list with negative indexing:", L2[-2])

L3 = [['Geeks', 'For'], ['Geeks']]
print("\nMulti Dimensional List: ", L3)
print("Accessing Multi Dimensional List:",L3[0][1])

#List slicing
L4= [10, 20, 14, 25, 30, 45, 50]
print("Slicing a List:",L4[:2],L4[1:3],L4[1:4],L4[4:])

#List functions
L5 = [10, 20, 14, 25, 30, 45, 50]
print("list:",L5)
L5.append(120)
print("Append:",L5)
L5.clear()
print("Clear:",L5)
L5 = L4.copy()
print("Copy:",L5)
print("count:",L5.count(20))
L5.extend(L4)
print("Extend:",L5)
print("count:",L5.count(20))
print("Index:",L5.index(25))
L7 = [10, 20, 30, 40, 50]
L7.pop(3)
print("Pop:",L7)
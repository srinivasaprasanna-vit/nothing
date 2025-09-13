t=input()
l=[]
for i in t:
   if i!=" ":
       l.append(int(i))

print('List1: ',l)
r=int(input())
l.remove(r)
print('List after removal: ',l)
a=input()
l2=[]
for i in a:
    if i!=" ":
        l2.append(int(i))
print(l2)
l.extend(l2)
print('Final List: ',l)
t=input()

l=[]
for i in t:
   if i!=" ":
       l.append(int(i))

print('List1:',l)
r=int(input())

try:
    l.remove(r)
    print('List after removal: ',l)
except:
    print("Element not found in the list")


a=input()
for i in a:
    if i!=" ":
        l.append(int(i))
print("Final List: ",l)
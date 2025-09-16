t=input()

l=[]
for i in t:
    tmp=""
    if i!=" ":
        tmp+=i
        l.append(int(tmp))


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
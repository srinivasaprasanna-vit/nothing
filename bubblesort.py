ar=[135,325,2512,123,12,45,78,90,23]

def bubble(ar):
    n=len(ar)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if ar[j]>ar[j+1]:
                ar[j],ar[j+1]=ar[j+1],ar[j]
    return ar
print(bubble(ar))
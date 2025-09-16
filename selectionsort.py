def selection_sort(ar):
    for i in range(len(ar)):
        min_i=i
        for j in range(0,min_i):
            if ar[j]>ar[min_i]:
                min_i=j
        ar[i],ar[min_i]=ar[min_i],ar[i]
    return ar
ar=[12,90,23]
print(selection_sort(ar))
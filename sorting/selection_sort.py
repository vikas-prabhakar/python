#!/usr/local/bin/python3.5
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_id=i
        for j in range(i+1,n):
            if arr[min_id] > arr[j]:
                min_id=j
        temp=arr[i]
        arr[i]=arr[min_id]
        arr[min_id]=temp


list = [14,47,21,59,45,22,1]
selection_sort(list)
print(list)

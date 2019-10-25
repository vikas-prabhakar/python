#!/usr/local/bim/python3.5
def insertion_sort(arr):
    n=len(arr)
    for i in range(n):
        current_val=arr[i]
        j=i
        while j >0 and current_val < arr[j-1]:
            arr[j]=arr[j-1]
            j=j-1
        arr[j]=current_val
list = [14,47,21,59,45,22,1]
insertion_sort(list)
print(list)

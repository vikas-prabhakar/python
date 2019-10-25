#! /usr/bin/python3.5
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
list = [14,47,21,59,45,22,1]
bubble_sort(list)
print(list)
    

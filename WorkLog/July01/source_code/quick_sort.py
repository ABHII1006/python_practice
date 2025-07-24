def quicksort(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2
    pivot=arr[mid]
    left_arr=[x for x in arr if x>pivot]
    right_arr=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    return quicksort(left_arr)+middle+quicksort(right_arr)

lst=[10,22,3,2,7]
print(quicksort(lst))
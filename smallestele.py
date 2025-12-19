def smallest_ele(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min

arr = [11,2,3,4,5,8,66,5,4,]
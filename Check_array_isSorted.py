# check array is sorted or not 

def isArray_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True


ans=isArray_sorted([1,6,4,4,5])
print(ans)
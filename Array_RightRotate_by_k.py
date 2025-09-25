# Array Right rotate by k position 
# Example :    [1,2,3,4,5] k=2 
# 1st rotation [5,1,2,3,4]
# 2nd rotation [4,5,1,2,3]


# Approach : using Reverse method 
# [1,2,3,4,5] --> reverse [5,4,3,2,1] --> reverse 0 t0 k-1 index [4,5,3,2,1] --> reverse kth to last [4,5,1,2,3]


def right_rotate(arr,k):
    k=k%len(arr)           # if k is greater than array size 
    reverse(arr,0,len(arr)-1)  # 1. reverse the full  arry 
    reverse(arr,0,k-1)         # 2. reverse the array 0th index to k-1 
    reverse(arr,k,len(arr)-1)  # 3. reverse the arry form kth index to last element 

    return arr

def reverse(arr,s,e):
    while s<e:
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1
    return arr


print(right_rotate([1,2,3,4,5],2))


# Array left rotate by k position 
# Example:               [1,2,3,4,5] and k= 2 position 
# 1st rotation of array: [2,3,4,5,1]
# 2nd rotation of array: [3,4,5,1,2]



def reverse(arr,s,e):
    
    while s<e:
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1
    return arr



def left_rotate(arr,k):
    k=k%len(arr)
    reverse(arr,0,k-1)
    reverse(arr,k,len(arr)-1)
    reverse(arr,0,len(arr)-1)
    return arr


print(left_rotate([1,2,3,4,5],2))
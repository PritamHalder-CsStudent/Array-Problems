# Second largest element in an array 
# if second largest element not found then return -1
# if all array element [5,5,5,5,5] are same then return -1 

def Second_Largest(arr):
    if len(set(arr))==1:  # checking  array elements are same or not . we convert the arry to set . set does not contain duplicate elements
        return -1         # if array contain duplicate elements then set contain only one element so length of set is '1' . 
    
    largest_ele=arr[0]
    sec_largest=-1
    for i in range(0,len(arr)):
        if arr[i] > largest_ele:
            sec_largest=max(largest_ele,sec_largest) # this will check largest_ele and sec_largest  using max() method
            largest_ele=arr[i]

        if arr[i] < largest_ele and arr[i] > sec_largest:
            sec_largest=arr[i]    
    return sec_largest



print(Second_Largest([1,5,9,7,4,3]))
            

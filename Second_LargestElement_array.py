# Second largest element in an array 

def Second_Largest(arr):
    largest_ele=arr[0]
    sec_largest=0
    for i in range(0,len(arr)):
        if arr[i] > largest_ele:
            sec_largest=max(largest_ele,sec_largest) # this will check largest_ele and sec_largest
            largest_ele=arr[i]

        if arr[i] < largest_ele and arr[i] > sec_largest:
            sec_largest=arr[i]    
    return sec_largest



print(Second_Largest([1,4,3,7,5]))
            

# merge two sorted array 
# Example: [1,2,3,4] , [5,7,8,9] ----> [1,2,3,4,5,7,8,9]

def merge_sorted_array(arr1,arr2):
    s1=0
    len1=len(arr1)
    s2=0
    len2=len(arr2)
    new_arr=[]  # temporary array to store result
    
    
    while s1 < len1 and s2 < len2:
        if arr1[s1] < arr2[s2]:   # compare elements from both array 
            new_arr.append(arr1[s1])
            s1+=1
        else:
           new_arr.append(arr2[s2])
           s2+=1
    #   copy remaining elements from arr1    
    while s1 < len1:
        new_arr.append(arr1[s1])
        s1+=1
    #   copy remaining elements from arr2     
    while s2 < len2:
        new_arr.append(arr2[s2])  
        s2+=1
   
    return new_arr




print(merge_sorted_array([6,9,10,23],[5,12,20]))

    
                   
             
                
        
# Subarray with Given sum problems 
# Example : [2,12,-2,-20,10]  ,  sum = -10 
# Output : Sum fount between indexes 1 to 3 and subarray is : [12, -2, -20]


# basic approach --> O(n^2)
def subarray_sum_basic(arr,Target):
    for i in range(len(arr)):
        curr_sum=0
        for j in range(i,len(arr)):
            curr_sum+=arr[j]
            if curr_sum == Target:
                return arr[i:j+1]
    return None

# print(subarray_sum_basic([2,12,-2,-20,10],-10)) 

# Best approach using map 
def subarray_sum(arr,Target):
    map={}
    start=0
    end=-1
    curr_sum=0
    for i in range(len(arr)):
        curr_sum+=arr[i]
        if curr_sum  == Target: # we found a subarray starting from indesx 0 and ending at i
            start=0
            end=i
            break
        if (curr_sum - Target) in map: # curr_sum - Target already exists in map, we found target sum
            start=map[curr_sum - Target]+1
            end=i
            break
        map[curr_sum]=i   #  if curr_sum not present in map then add to map 
        
    return arr[start:end+1]   

print(subarray_sum([2,12,-2,-20,10],-10)) 

          

    
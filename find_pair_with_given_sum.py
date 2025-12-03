# Find pair with given sum : Two sum problem

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# Example
#Input: nums = [3,2,4], target = 6
#Output: [1,2] index num of the elements

# time complexity  O(n^2)  Approach:
def pair(arr,target):
    
    for i in range (0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target :
                return [i,j]
    return []

print(pair([3,2,4],6))  
   

# best approach --> time complexity  O(n) and space complexity also O(n) 

def target_pair(nums,target):
    map={}
    for i in range(0,len(nums)):
        rem=target-nums[i]      # calculating remaining part 
        if rem in map:      # if rem already present we fount the match element to get target
            return [map[rem],i]
        map[nums[i]]=i   # if remaining part not present in the map data structure then add only element to the map 
    return []        


print(target_pair([3,2,4],6))    
            
            
            
                

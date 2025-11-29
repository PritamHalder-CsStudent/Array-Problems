# Given an array arr[] denoting heights of n towers and a positive integer k.
'''
For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by k
Decrease the height of the tower by k

Find out the minimum possible difference between the height of the shortest 
and tallest towers after you have modified each tower.
'''

# Input: k = 2, arr[] = [1, 5, 8, 10]
# Output: 5
# Explanation: The array can be modified as [1+k, 5-k, 8-k, 10-k] = [3, 3, 6, 8]. 
# The difference between the largest and the smallest is 8-3 = 5.

# Input: k = 3, arr[] = [3, 9, 12, 16, 20]
# Output: 11
# Explanation: The array can be modified as [3+k, 9+k, 12-k, 16-k, 20-k] = [6, 12, 9, 13, 17]. 
# The difference between the largest and the smallest is 17-6 = 11.


class Solution:
    def getMinDiff(self, arr, k):
        n=len(arr)
        arr.sort()
        
        ans=arr[-1]-arr[0] # initial diff 
        
        for i in range(n-1):
            high=max(arr[i]+k,arr[-1]-k)  # indices 0 to i → increase by k
            low=min(arr[0]+k,arr[i+1]-k)  # indices i+1 to n-1 → decrease by k
            
            if low<0:  # remove negative value 
                continue
            ans=min(ans,high-low)
            
        return ans    
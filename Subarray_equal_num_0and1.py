# Given a binary array nums, 
# return the maximum length of a contiguous subarray with an equal number of 0 and 1.

'''
Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Example 3:
Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.

'''
# best approach using O(N) 
# Convert 0 to -1 Logic Internally
#   0 → -1
#   1 → +1

class Solution:
    def findMaxLength(self, nums):
        mp = {0: -1}  # prefixSum first occurrence
        prefixSum = 0
        maxi = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prefixSum -= 1
            else:
                prefixSum += 1

            if prefixSum in mp:
                maxi = max(maxi, i - mp[prefixSum])
            else:
                mp[prefixSum] = i

        return maxi


#Using basic Approach this will take O(n^3)
class Solution:
    # check equal num of '1' and '0' present in subarray 
    def solve(self,arr): 
        countOne=0
        countZero=0
        for ele in arr:
            if ele==1:
                countOne+=1
            else:
                countZero+=1
        if countOne==countZero:
            return countOne+countZero
        return -1            


    def findMaxLength(self, nums: List[int]) -> int:
        if len(set(nums))==1:
            return 0
        n=len(nums)
        maxi=float('-inf')
        for i in range(0,n):
            for j in range(i+1,n):
              maxi=max(maxi,self.solve(nums[i:j+1])) # generate all possible subarray and check equal num of '0' and '1'
        return maxi
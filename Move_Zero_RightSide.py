# Move zero right side of the array 
# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        nonZeroIndx=0
        for ele in nums:
            if ele!=0:
                nums[nonZeroIndx]=ele
                nonZeroIndx+=1

        while nonZeroIndx<n:
            nums[nonZeroIndx]=0
            nonZeroIndx+=1


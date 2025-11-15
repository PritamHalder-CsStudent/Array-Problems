#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
#nand two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing orde


# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


# Approach:
# I did not take extra  data structure(list) to store the array elements 
#  merge the array from the ending of the list 


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1=m-1        #last index of nums1
        p2=n-1        # last index of nums2
        indx=m+n-1    # index that help to store list element form ending position 

        while p1>=0 and p2>=0:
            if nums1[p1]>=nums2[p2]: # if nums1[p1] is largest element then it stor at last index of num1 list 
                nums1[indx]=nums1[p1]
                indx-=1
                p1-=1
            else:
                nums1[indx]=nums2[p2]
                indx-=1
                p2-=1

        while p1>=0:
            nums1[indx]=nums1[p1]
            indx-=1
            p1=p1-1
        while p2>=0:
            nums1[indx]=nums2[p2]
            indx-=1
            p2=p2-1

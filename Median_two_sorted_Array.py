# Median-->the  middle element of sorted list 
# if length of the list is odd then , median is middle of the list element 
# Example : [2,5,7]-- > 5 is median 

# if length of list is even then , median is  element of ((midIndex-1) + midIndex)/2
# Example : [4,6,8,10] --> (6+8)/2=7 is median 


# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# Example 1:
'''
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''
# Example 2:
'''
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5
'''

class Solution:
    def mergeArray(self,nums1,nums2,res):
        p1=0
        p2=0
        m=len(nums1)
        n=len(nums2)
        while p1<m and p2<n:
            if nums1[p1]<=nums2[p2]:
                res.append(nums1[p1])
                p1+=1
            else:
                res.append(nums2[p2])
                p2+=1

        # if some elements are left at nums1
        while p1<m :
            res.append(nums1[p1])
            p1+=1
        # if some elements are left at nums2    
        while p2<n :
            res.append(nums2[p2])
            p2+=1
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=[]
        self.mergeArray(nums1,nums2,res) # merge the sorted array 
        length=len(res)
        if length%2!=0: # length of res arr is odd then
            mid=int(length/2) # list index does not float value
            return res[mid]
        
        #length of res arr is even then 
        mid=int(length/2) # list index does not float value , so used int() for typecasting 
        return (res[mid-1]+res[mid])/2

# maximum sub array sum 
# Array num element is n then total possible sub arrays: n*(n+1)/2

# Example : [5,4,-1,7,-8]  --->  All possible sub Arrays : [5],[4],[-1],[7],[-8],[5,4],[4,-1],[-1,7],[7,-8],
#                                                         [5,4,-1],[4,-1,7],[-1,7,-8],[5,4,-1,7],[4,-1,7,-8]
#                                                         [5,4,-1,7,-8]

# maximum sub array sum is = 15 , ans sub array is : [5,4,-1,7]

# Basic Approach using O(N^2):
def maxSubarraySum(arr):
    res = arr[0]
  
    # Outer loop for starting point of subarray
    for i in range(len(arr)):
        currSum = 0
      
        # Inner loop for ending point of subarray
        for j in range(i, len(arr)):
            currSum = currSum + arr[j]
          
            # Update res if currSum is greater than res
            res = max(res, currSum)      
    return res


# Another method that will also work all negative element array and mixed element  

# Approach:
# maxEnding at index i = max(maxEnding at index (i - 1) + arr[i], arr[i]) and 
# the maximum value of maxEnding at any index will be our answer.
# Time complexity--O(N)

def find_maxSubarraySum(self, arr):
        res = arr[0]
    # Maximum sum of subarray ending at current position
        maxEnding = arr[0]

        for i in range(1, len(arr)):
        # Either extend the previous subarray or start 
        # new from current element
            maxEnding = max(maxEnding + arr[i], arr[i])
        # Update result if the new subarray sum is larger
            res = max(res, maxEnding)
        return res



# when all array element are negative this will not found the maximum sub array sum
# This function will give maximum subarray sum with answer subarray 
def maximum_Subarray_sum(arr):
    sum=0
    maxi=0
    startIndx=0 
    endIndx=0
    for i in range(0,len(arr)):
        if sum == 0:            # when sum = 0  then it represent start of subarray 
            start=i
        sum+=arr[i]
        if sum > maxi:
            maxi=sum
            startIndx=start
            endIndx=i       # last iteration of array where sum is positive value , it is used to end Index of sub array
        if sum < 0:         # if sum goes to negative value , then sum re initialize to zero 
            sum=0
    return maxi, arr[startIndx:endIndx+1]   


print(maximum_Subarray_sum([5,4,-1,7,-8]))        
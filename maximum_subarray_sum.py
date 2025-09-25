# maximum sub array sum 
# Array num element is n then total possible sub arrays: n*(n+1)/2

# Example : [5,4,-1,7,8]  --->  All possible sub Arrays : [5],[4],[-1],[7],[8],[5,4],[4,-1],[-1,7],[7,8],
#                                                         [5,4,-1],[4,-1,7],[-1,7,8],[5,4,-1,7],[4,-1,7,8]
#                                                         [5,4,-1,7,8]

# maximum sub array sum is = 15 , ans sub array is : [5,4,-1,7]





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
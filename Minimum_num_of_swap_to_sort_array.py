# find minimum num of swap to sort an array 

# Examples:
#Input: arr[] = [2, 8, 5, 4]
#Output: 1
#Explanation: Swap 8 with 4 to get the sorted array.

#Input: arr[] = [10, 19, 6, 3, 5]
#Output: 2
#Explanation: Swap 10 with 3 and 19 with 5 to get the sorted array.


class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, arr):
	    temp=sorted(arr) # create sorted array with name temp 
	    pos={}    # pos dict will store array element wise index num (arr[i]-->i)
	    swap=0    # help to count swap 
	    
	    for i in range(len(arr)): # store array element wise index num (arr[i]-->i)
	        pos[arr[i]]=i
	   
	    for i in range(len(arr)):
	        
	       # if arr element and temp element are not same then go
	        if arr[i]!=temp[i]:
	            
	            indx=pos[temp[i]] # find position of temp element 
	           
	            arr[i],arr[indx]=arr[indx],arr[i]  # now swap with ith position and indx position at orginal arr
	            swap+=1  # count swap 
	           
	            # reset the dictionary element wise index
	            pos[arr[i]]=i
	            pos[arr[indx]]=indx
             
	    return swap        
		
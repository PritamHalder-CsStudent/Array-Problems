# find the minimum number of jumps needed to move from the first position in the array to the last position.
# If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
# If arr[i] = 0, you cannot jump forward from that position.

# Return -1 if you can't reach the end of the array.
# Example 1:  arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# Output: 3 
# Explanation: First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, 
# and from here we will jump to the last.

# arr = [0, 10, 20]
# Output: -1
# Explanation: We cannot go anywhere from the 1st element. 

def minJumps(arr):
	n=len(arr)
	if n<=1:
	    return 0
	if arr[0]==0:
	    return -1
	jumps=1             # we start with first jump from index 0 
	maxReach=arr[0]     # farthest index reachable so far 
	steps=arr[0]        # steps we can still take in current jump
	    
	for i in range(1,n):
	    if i==n-1:  # if we reach last index , return jumps
	        return jumps
	    maxReach=max(maxReach,i+arr[i]) 
	    steps-=1
	        
	    if steps==0:
	        jumps+=1
	        if i>=maxReach:
	            return -1     
	        steps=maxReach-i
	return -1 

print(minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))   

 


	        
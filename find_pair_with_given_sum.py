# Find pair with given sum 
# Example: [1,2,3,4,5], sum=6  --> (1,5),(2,4)

def pair(arr,target):
    ans={}
    for i in range (0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target :
                ans[arr[i]]=arr[j]
    return ans

print(pair([1,2,3,4,5],6))    


# best approach --> time complexity  O(n) and space complexity also O(n) 

def target_pair(arr,target):
    ans=[]
    seen=set()
    for ele in arr:
        complement=target-ele
        if complement  in seen:
            ans.append((ele,complement))
        seen.add(ele)
    return ans


print(target_pair([1,2,3,4,5],6))    
            
            
            
                

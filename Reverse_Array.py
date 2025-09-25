# Reverse a array
# Reverse array using two pointer approach

def reverse_array(arr):
    s=0
    e=len(arr)-1
    while s<=e:
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1
    return arr


# take array input using user 
l=int(input("Enter num of elements:"))
arr=[]
for i in range(0,l):
    arr.append(int(input())) # taking input one by one 
print("Orginal input arr:",arr)

# function call 
ans=reverse_array(arr)
print("Reverse array is:",ans)
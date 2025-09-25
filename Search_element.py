# Search an element in given array

def search_element(arr,ele):
    if ele in arr:
        return True
    return False



#arr=[5,6,7,89,3,4]

# take array input using user 
l=int(input("Enter num of elements:"))
arr=[]
for i in range(0,l):
    arr.append(int(input())) # taking input one by one 
print("Orginal input arr:",arr)

# function call
ans=search_element(arr,89)
print(ans)
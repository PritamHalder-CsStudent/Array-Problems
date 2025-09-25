# Find missing number in a array sequance 
# Example : [1,2,4,5] --> the missing element is 3 

# Approach :
# Using XOR approach,  same element a^a = 0  , 2 ^ 2 =0
#                      different element a^b != 0  , 2 ^ 3 = 2 ^ 3  



def missing_element(arr):
    xor1=arr[0]
    for i in range(1,len(arr)):
        xor1=xor1^arr[i]         

    xor2=1
    end=arr[-1]
    for i in range(2,end+1):
        xor2=xor2^i

    return xor1 ^ xor2


print(missing_element([1,2,4,5]))
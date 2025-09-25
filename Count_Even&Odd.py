# count number of Even and Odd elements present in array

def count_even_odd(arr):
    even_count=0
    odd_count=0
    for ele in arr:
        if ele %2 == 0:
            even_count+=1
        else:
            odd_count+=1
    return [even_count,odd_count]



arr=[1,2,3,4,5]
ans=count_even_odd(arr)
print(ans)
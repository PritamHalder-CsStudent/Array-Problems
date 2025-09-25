# Find frequency of each element 

def find_frequency(arr):
    freq={}
    for ele in arr:
       freq[ele]=freq.get(ele,0) +1     
       

    return freq

# different way to use dicttonary 

def another_way(arr):
    freq={}
    for ele in arr:
        if ele in freq:
            freq[ele]+=1
        else:
            freq[ele]=1
    for key,value in freq.items():
        print(f"{key}:{value} times")


print(another_way([1,2,2,3,4,5,3,4,7]))

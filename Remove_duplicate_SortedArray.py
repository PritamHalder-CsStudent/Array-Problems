# Remove duplicate from sorted array 

def remove_duplicate(arr):
    visit=set()            # using set remove duplicate 
    for ele in arr:
        if ele not in visit:
            visit.add(ele)
    return list(visit)        # convert set object to list data structure 
    


print(remove_duplicate([1,2,2,2,3,4,4,5]))


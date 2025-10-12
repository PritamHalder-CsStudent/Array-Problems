# Find duplicate elements in array 
# Example: [2,3,4,2,5,7,5,9] ----> duplicate element -> 2, 5


def find_duplicate(arr):
    map={}
    for ele in arr:
        map[ele]=map.get(ele,0) + 1
    for key in map:
        if map[key] >=2 :
            print(key)
    return None

print(find_duplicate([2,3,4,2,5,7,5,9]))


            
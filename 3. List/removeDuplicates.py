# Better Approach
def remDup(arr):
    n = len(arr)
    res = 1
    for i in range(1, n):
        if(arr[res-1] != arr[i]):
            arr[res] = arr[i]
            res+=1

print(remDup([1,1,2,2,3,3,4,4,5]))

# or
def removeDup(arr):
    newSet = set()

    for i in arr:
        newSet.add(i)

    return len(list(newSet))

print(removeDup([1,1,2,2,3,3,4,4,5]))
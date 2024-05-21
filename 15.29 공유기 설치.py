n ,c = map(int, input().split)
array = []
for i in range(n):
    x = int(input())
    array.append(x)
array.sort()
# [1,2,4,8,9] c 3개 
def first(array,target,start,end):
    if start > end:
        return None
    mid = (start + end)//2
    if array[mid]
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid -1)
    else:
        return first(array,target,mid +1, end)
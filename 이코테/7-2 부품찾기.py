#부품n, 찾으려는 개수 m
'''
ex) 5           
    2 4 6 9
    3
    1 2 3
'''
#no yes no
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
result = []
m_list = list(map(int, input().split()))
count = 0
for i in range(len(m_list)):
    for k in n_list:
        if m_list[i] ==k:
          result.append('yes')
        else:
            continue
    if len(result) != i+1:
        result.append('no')
    else:
        continue
print(*result)
##########################
def binury_search(array,target,start,end):
    if start > end:
        return None
    mid = (start +end)//2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binury_search(array, target,start, mid -1)
    else:
        return binury_search(array,target,mid +1,end)
    
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
result = []
m_list = list(map(int, input().split()))

a = binury_search(n_list,m_list,n_list[0],n_list[n-1])
if not a == None:
    result.append('no')
else:
    result.append('yes')
print(*result)
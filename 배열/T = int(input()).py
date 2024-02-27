N,M = map(int, input().split())
list = [0]*N

for i in range(1,M+1):
    i,j,k = map(int, input().split())
    for i in range(i-1,j):
        list[i] = k

print(" ".join(map(str, list)))
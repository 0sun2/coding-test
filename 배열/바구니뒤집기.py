N,M = map(int, input().split())
list = []
for i in range(N):
    list.append(i+1)
for i in range(M):
    i,j = map(int, input().split())
    list[i-1:j] = reversed(list[i-1:j])

print(" ".join(map(str, list)))
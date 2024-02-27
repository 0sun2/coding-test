
n = int(input())
x,y = 1,1
plans = input().split()
move_list = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in plans:
    for k in range(len(move_list)):
        if i == move_list[k]:
            nx = x + dx[k]
            ny = y + dy[k]
    if nx <= 0 or ny <= 0 or nx > n or ny > n:
            continue
    x, y = nx, ny
print(x,y)


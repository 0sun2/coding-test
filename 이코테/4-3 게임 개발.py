# N * M 크기의 직사각형 각각의 칸은 육지 또는 바다
#캐릭터는 동서남북 중 한 곳을 바라본다.
#맵의 각 칸은 (A,B) A는 북쪽으로 부터 떨어진 칸의 개수 , B는 서쪽으로 부터 떨어진 칸의 개수 
#바다는 못감
'''
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정함
2. 캐릭터의 바로 왼쪽 방향에 가보지 않은 칸이 존재한다면,왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸 전진. 가보지 않은 칸이 없다면 회전만 하고 1번으로
3.모드 가본 칸이거나 바다라면, 바라보는 방향을 ㅇ지하고 한칸 뒤로 가고 1단계로, 만약 뒤가 바다이면 움직임을 멈춤
'''
# 첫째줄에 세로 N 가로 M 입력
#둘째 줄에 캐릭터가 있는 좌표 (A,B) 글고 바라보는 방향 d
# 셋째 줄부터 지형
#북동남서 0123
n, m = map(int, input().split()) #세로 n 가로 m
x, y, direction  = map(int, input().split()) #(a,b)는 캐릭터 위치 d는 보는 방향

map_list = [] #맵을 받을 리스트
for i in range(n):
    map_list.append(list(map(int, input().split()))) #[[1,1,1,0],[1,1,0,0],[0,0,0,0],[1,0,1,0]
dx= [-1,0,1,0]
dy = [0,1,0,-1]

map_list[x][y] = 1
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if map_list[nx][ny] == 0:
        map_list[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
    else:
        turn_time += 1
    if turn_time ==4:
        nx = x -dx[direction]
        ny = y -dy[direction]
        if map_list[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
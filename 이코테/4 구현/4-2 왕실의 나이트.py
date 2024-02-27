
locate = str(input())
x_num = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8}
x,y = x_num[locate[0]],locate[1]

#나이트가 이동할 수 있는 최대 경우의 수 8가지
steps = [(-1,-2),(1,-2),(-1,2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]

result = 0
for step in steps:
    new_x, new_y = x + step[0], int(y) + step[1]
    if new_x <= 0 or new_y <= 0 or new_x>= 9 or new_y>= 9:
        continue
    else:
        result += 1
    
print(result)
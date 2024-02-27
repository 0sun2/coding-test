# 정수n 입력 0시0분0초부터 n시 59분59초까지의 모든 시각중에 3이 하나라도 포함되는 경우의 수를 구하라
n = int(input())
time = [0,0,0]
count = 0
for hour in range(n+1):
    time[0] = hour
    for minute in range(60):
        time[1] = minute
        for second in range(60):
            time[2] = second
            if any('3' in str(i) for i in time):
                count += 1

print(count)


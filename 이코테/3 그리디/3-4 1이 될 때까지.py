'''
N이 1이 될 때까지 
1.N에서 1을 뺀다.
2. N을 K로 나눈다 (N이 K로 나누어떨어질 때만)
EX) N= 17 K= 4 
1번 -> 16 2번 -> 4 -> 1 
출력 - 최소횟수
'''
import time

n, k = map(int, input().split())
start_time = time.time()
count = 0
# k로 나누어질 때까지 빼고 나누기 
while True:
    if n%k == 0:
        n = n/k
        count += 1
    else:
        n -= 1
        count += 1
    if n == 1:
        break
print(count)
end_time = time.time()
print("time:", end_time - start_time)
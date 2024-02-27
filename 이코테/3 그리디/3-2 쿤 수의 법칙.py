#배열의 크기 N
#숫자가 더해지는 횟수 M
#연속해서 더할 수 있는 횟수 K

N, M, K = map(int, input().split())
#배열
array = list(map(int, input().split()))
array.sort()
max_val = array[N-1]
second_max_val = array[N-2]
count = 0

while True:
   for i in range(K):
      if M == 0:
         break
      count += max_val
      M -= 1
   if M == 0:
      break
   count +=second_max_val
   M -= 1
print(count)
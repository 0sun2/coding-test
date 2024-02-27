#N은 행
#M은 열

#먼저 뽑고 싶은 행(N)을 선택 -> 그 행에서 가장 낮은 카드를 뽑아야함

N, M =map(int, input().split())
min_val_list = []
for i in range(N):
    card_list = list(map(int, input().split()))
    min_val = min(card_list)
    min_val_list.append(min_val)

result = max(min_val_list)
print(result)
#### 책 풀이 
N, M =map(int, input().split())
result = 0
for i in range(n):
    data= list(map(int, input().split()))
    min_value = min(data)
    result= max(result, min_value)
print(result)
def solution(N, stages):
    result_list = []
    answer = []
    for i in range(N):
        total = 0
        count = 0
        result = 0
        for j in stages:
            if j > i:
                total += 1
            elif j == i+1:
                count += 1
                total += 1
            else:
                continue
        if not count == 0:
          result = count / total
        result_list.append((i+1,result))
    result_list.sort(key = lambda x: - x[1])
    for item in result_list:
        answer.append(item[0])

    return answer

N = int(input())
stages = list(map(int, input().split()))
solution(N,stages)
my_list = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score_list = []
credit_sum = 0
for i in range(20):
    a,b,c = input().split()
    if c not in my_list:
        pass
    elif c == 'F':
        credit_sum += float(b)
    else:
        grade = float(b) * (4.5 - my_list.index(c)/2)
        score_list.append(float(grade))
        credit_sum += float(b)
score_sum = sum(score_list)
print(score_sum/credit_sum)
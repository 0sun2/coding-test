n = int(input())
student_list = []
for i in range(n):
    student_list.append(input().split())
student_list.sort(key= lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for student in student_list:
    print(student[0])

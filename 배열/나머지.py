my_list= []
for i in range(10):
    n = int(input())
    a = n%42
    my_list.append(a)
another = []
for i in my_list:
    if i not in another:
        another.append(i)
print(len(another))
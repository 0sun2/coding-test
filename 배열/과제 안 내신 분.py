my_list = list(range(1,31))
for i in range(28):
    a = int(input())
    my_list.remove(a)
my_list.sort()
min_val = my_list[0]
max_val = my_list[1]

print(min_val)
print(max_val)
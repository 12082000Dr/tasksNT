n, m = map(int, input().split()) #n - длинна, m - шаг
result_list = list(range(1, m + 1))

while result_list[-1] != 1:
    last_value = result_list[-1] #последние значение
    len_list = list(range(last_value, n + 1)) + list(range(1, last_value))
    for i in len_list[:m]:
        result_list.append(i)

index = 0
path_list = []
for j in range(int(len(result_list) / m)):
    path_list.append(result_list[index])
    index += m
print(*path_list, sep='')
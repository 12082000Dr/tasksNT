with open(input()) as integers_read:
    integers = map(int, integers_read.read().split('\n'))

integer = [int(i) for i in integers]
medium_value = round(sum(integer) / len(integer))

count = 0

while integer.count(medium_value) != len(integer):
    index = 0
    for i in integer:
        if i < medium_value:
            integer[index] = i + 1
            count += 1
            index += 1
        elif i > medium_value:
            integer[index] = i - 1
            count += 1
            index += 1
        else:
            index += 1
            continue
print(count)

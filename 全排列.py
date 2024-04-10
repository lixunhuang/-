def arrange(array, result, total):
    if len(array) == len(result):
        total.append([x for x in result])
        return

    for index, element in enumerate(array):
        if element not in result:
            result.append(element)
            arrange(array, result, total)
            result.pop()
        i = index
    if i == len(array) - 1:
        return total


total = arrange([4, 2, 3, 1, 5], [], [])
t = len(total)
print(t)
for i in total:
    print(i)

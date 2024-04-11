def queen(choices: list, result: list, total: list, row):
    if len(choices) == len(result):
        total.append(result.copy())
        return
    for i in choices:
        if i not in result:
            do = True
            for x, y in enumerate(result):
                if abs(row - x - 1) == abs(i - y):
                    do = False
            if do:
                result.append(i)
                queen(choices, result, total, row + 1)
                result.pop()


total = []
queen([1, 2, 3, 4, 5], [], total, 1)
for i in total:
    print(i)

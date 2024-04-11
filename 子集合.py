def son_set(choices: list, result: list, sum: int, total: list, num:int):
    if sum == 10:
        total.append(result.copy())
        return
    for i in choices:
        if i + sum <= 10 and i >= num:
            sum = sum + i
            result.append(i)
            son_set(choices, result, sum, total, i)
            result.pop()
            sum = sum - i


total = []
son_set([1, 2, 3, 4, 5], [], 0, total, 0)
for i in total:
    print(i)

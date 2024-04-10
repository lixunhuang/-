def search(array, target):
    if len(array) <= 1:
        return array[0]
    mid = len(array) // 2
    left_array = array[0:mid]
    right_array = array[mid:]
    if target < left_array[0] or target > right_array[-1]:
        return None
    if target <= left_array[-1]:
        new_array = search(left_array, target)
    elif target >= right_array[0]:
        new_array = search(right_array, target)
    return new_array


if search([0, 1, 2, 3, 4, 5], 7):
    print('yes')

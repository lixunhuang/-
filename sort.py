def sort(array):
    left, right = 0, len(array)
    if len(array) == 2:
        if array[1] > array[0]:
            return array
        else:
            array[1], array[0] = array[0], array[1]
            return array
    elif len(array) == 1:
        return array
    mid = len(array) // 2
    left_array = array[left:mid]
    right_array = array[mid:right]
    i = 0
    new = []
    while i < min(len(left_array), len(right_array)):
        if left_array[i] < right_array[i]:
            new.append(left_array[i])
        else:
            new.append(right_array[i])
        i+=1




def merge():



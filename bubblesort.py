def bubbleSort(lst):

    length_array = len(lst) - 1
    sorted = False

    while not sorted:
        
        sorted = True

        for i in range(length_array):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sorted = False
        length_array -= 1

    return lst


lst = [5, 4, 3, 2, 1]

sorting = bubbleSort(lst)

print(sorting)

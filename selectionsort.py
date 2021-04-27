def selectionSort(lst):

    for i in range(len(lst)):
        lowestNumberIndex = i
        for j in range(i + 1, len(lst)):
            if lst[lowestNumberIndex] > lst[j]:
                lowestNumberIndex = j
        lst[i], lst[lowestNumberIndex] = lst[lowestNumberIndex], lst[i]

    return lst


lst = [5, 4, 3, 2, 1]

print(selectionSort(lst))

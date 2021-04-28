def insertionSort(lst):
    for index in range(1, len(lst)):
        lst_temp = lst[index]
        comp_index = index - 1

        while comp_index >= 0:
            
            if lst[comp_index] > lst_temp:
                lst[comp_index + 1] = lst[comp_index]
                comp_index -= 1
            else:
                break
        lst[comp_index + 1] = lst_temp
    return lst

lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(insertionSort(lst))

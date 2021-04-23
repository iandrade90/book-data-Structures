
def linearsearchorderedarray(array, data):

    for element in array:
        if element == data:
            return 'The searched element is at index {}'.format(array.index(element))
        elif element > data:
            return None

array = [1, 3, 5, 7, 9]
data = 9

print(linearsearchorderedarray(array, data))

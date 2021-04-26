def binarysearch(array, data):

    bottomElement = 0
    topElement = len(array) -1

    while bottomElement <= topElement:

        middlePoint = int((topElement + bottomElement) /2)
        valueMidPoint = array[middlePoint]

        if data == valueMidPoint:
            return 'Value found at index {}'.format(middlePoint)
        elif data < valueMidPoint:
            topElement = middlePoint -1
        elif data > valueMidPoint:
            bottomElement = middlePoint +1

        if data not in array:
           return None


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
data = 20

print(binarysearch(array, data))

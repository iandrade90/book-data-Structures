def linearSearch(array, data):

    counter = 0

    sizeOfArray = len(array) - 1

    while counter < sizeOfArray:

        for element in array:
            if element == data:
                print('The element searched is at index {}'.format(counter))
            counter += 1

        if data not in array:
            print(None)

array = [4,2,8,4,1,4]
data = 4

linearSearch(array, data)

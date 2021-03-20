# Sorting Algorithm
# Insertion Sorting

def insertion_sort(array):

    for index in range(1, len(array)):
        temp_value = array[index] # Temporary value
        position = index - 1 # Value to compare

        while position >= 0:

            if array[position] > temp_value:
                array[position + 1] = array[position]
                position = position - 1
            else:
                break
        array[position + 1] = temp_value
    return array


# -----------------------------
#Quick Sorting
def qicksort(array):
    from random import randint
    if len(array) < 2:
        return array

    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)] #random number, ideally it should be a meadian

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return qicksort(low) + same + qicksort(high)


#Ja sašķirojamais datu masīvs ir mazāks par X, tad šķirošanai izmantot insertion sort, pretējā gadījumā šķirošanai izmantot quicksort
def sort_array(array):
    if len(array) <= 5:
        print('Insertion sort Algorithm!')
        return insertion_sort(array)
    else:
        print('Qicksort Algorithm!')
        return qicksort(array)


print(sort_array([1,3,2,4,5]))
print(sort_array([1,3,2,4,5,9,2,8,6,7]))

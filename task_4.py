unsorted_list = [5,4,3,2,1]

def bubble_sort_list(list):
    unsorted_until_index = len(list) - 1
    sorted = False
    step_count = 0
    swap = 0

    while not sorted:
        sorted = True
        for index in range(unsorted_until_index):
            step_count += 1
            if list[index] > list[index + 1]:
                list[index], list[index+1] = list[index+1], list[index]
                swap += 1
                sorted = False
        unsorted_until_index -= 1

    print(f'Cycles: {step_count}, Swaps: {swap}, Steps total: {step_count+swap}')
    return list

print(bubble_sort_list(unsorted_list))

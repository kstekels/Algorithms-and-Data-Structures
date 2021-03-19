# Key = identity ???
# def find_index(elements, value, key):
def find_index(elements, value):
    left = 0
    right = len(elements) - 1

    while left <= right:
        print('In while')
        middle = (left + right) // 2
        print(middle)
        # middle_element = key(elements[middle])
        middle_element = elements[middle]
        if middle_element == value:
            return middle
        if elements[middle] < value:
            left = middle + 1
        if elements[middle] > value:
            right = middle + 1

# def contains(elements, value, key = identity):
def contains(elements, value):
    return find_index(elements, value)
    # return find_index(elements, value, key)

# def find_iterative(elements, value, key = identity):
def find_iterative(elements, value):
    index = find_index(elements, value)
    # index = find_index(elements, value, key)
    return None if index is None else elements[index]


print(f"Contains (func): {contains([1,2,3,4,5,6,7,8,9], 0)}")
print(f"Find iteratives (func): {find_iterative([1,2,3,4,5,6,7,8,9], 10)}")


# 1. Key = identity???
# 2. find_iterative retuns the same number value ???
# 3. Infinity while loop, if value is = 0, because left == right == 0 and while will never end!

list_of_nums = [i for i in range (101)]

# O(log N)
def search_number(number, list):
    if number > list[-1]:
        return False
    else:
        left = 0
        right = len(list) - 1
        step_counter = 0
        while left <= right:
            middle = int((left + right)/2)
            step_counter += 1
            print(f'Searching for: {number}, left: {left}, right: {right}, middle: {middle}, step: {step_counter}')
            if number == middle or number == right or number == left:
                return f'Number of steps : {step_counter}'
            elif number < middle:
                right = middle + 1
            elif number > middle:
                left = middle - 1

print(search_number(50, list_of_nums))

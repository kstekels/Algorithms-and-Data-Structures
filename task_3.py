list_of_nums = [i for i in range (1, 101)]

def search_number(number, list):
    count = 0
    for num in list:
        count +=1
        if num == number:
            return f'Number: {number}, steps: {count}'
    return f'Number {number} is not in list'



print(search_number(10, list_of_nums))

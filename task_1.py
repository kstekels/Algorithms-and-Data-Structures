list_of_nums = [i for i in range (1, 101)] # 1 - 100

# O(1)
def remove_last_number(list):
    list.pop()
    return list


print(remove_last_number(list_of_nums))

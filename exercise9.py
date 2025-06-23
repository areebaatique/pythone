def find_max(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

print(find_max([3, 9, 2, 5, 8]))


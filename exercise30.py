def safe_access(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return "Index out of range."

# Example:
items = [1, 2, 3]
print(safe_access(items, 1))
print(safe_access(items, 5))


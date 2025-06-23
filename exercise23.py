def count_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return len(lines)

# Example usage (make sure to have 'test.txt'):
# print(count_lines("test.txt"))


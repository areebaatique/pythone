def count_letter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count

print(count_letter("banana", "a"))  # Output: 3


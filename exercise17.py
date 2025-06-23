def find_duplicates(items):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

# Example usage:
print(find_duplicates([1, 2, 3, 2, 4, 5, 1, 6]))


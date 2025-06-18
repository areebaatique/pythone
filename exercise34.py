# Sort names by length
names = ["Sara", "Areeba", "Ali", "Jonathan"]
sorted_names = sorted(names, key=lambda name: len(name))

# Filter positive numbers
numbers = [-5, 3, 0, 2, -1, 10]
positives = list(filter(lambda x: x > 0, numbers))

print("Sorted names by length:", sorted_names)
print("Positive numbers:", positives)

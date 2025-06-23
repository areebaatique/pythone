import random

# Generate 10 random numbers
random_nums = [random.randint(1, 100) for _ in range(10)]
print("Random numbers:", random_nums)

# Find the largest number
print("Largest number:", max(random_nums))

# Simulate rolling two dice 100 times
doubles = 0
for _ in range(100):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 == die2:
        doubles += 1

print("Doubles rolled in 100 tries:", doubles)


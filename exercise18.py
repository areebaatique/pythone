def simple_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    above_avg = sum(1 for n in numbers if n > average)
    return total, average, above_avg

# Example usage:
nums = [10, 20, 30, 40, 50]
total, avg, count_above = simple_stats(nums)
print("Sum:", total)
print("Average:", avg)
print("Numbers above average:", count_above)


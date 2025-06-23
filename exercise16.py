def sort_numbers(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

print(sort_numbers([5, 2, 9, 1, 7]))


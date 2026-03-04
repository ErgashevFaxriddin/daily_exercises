def second_largest(nums):
    unique_nums = list(set(nums))
    unique_nums.sort()
    return unique_nums[-2]

print(second_largest([10, 5, 8, 20, 20, 19]))
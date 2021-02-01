def sum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[-1] + sum(nums[:-1])


print(sum([5, 5, 5, 5, 5]))
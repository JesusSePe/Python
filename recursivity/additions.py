def sum(nums):
    # once there are no more numbers on the list, returns the last number.
    if len(nums) == 1:
        return nums[0]
    # The last item on list + all the other items.
    else:
        return nums[-1] + sum(nums[:-1])


print(sum([5, 5, 5, 5, 5]))
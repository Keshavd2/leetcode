def two_sum (nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [i, seen[complement]]
        else:
            seen[num] = i
    return []



print(two_sum([3, 2, 4], 6))
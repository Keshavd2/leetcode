def subarray_sum(nums, k):
    current_sum = 0
    counts = {0:1}
    result = 0

    for num in nums:
        current_sum += num
        result += counts.get(current_sum - k, 0)
        counts[current_sum] = counts.get(current_sum, 0) + 1
    
    return result


    

# Tests
print(subarray_sum([1, 1, 1], 2))     # Expected: 2
print(subarray_sum([1, 2, 3], 3))     # Expected: 2
print(subarray_sum([1, -1, 1], 1))    # Expected: 3
print(subarray_sum([0, 0, 0], 0))     # Expected: 6
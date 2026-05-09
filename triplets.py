def count_triplets(nums, k):
    count = 0

    for i in range(len(nums)):
         
        remainder_freq = {}

        for l in range(i + 2, len(nums)):
            r = nums[l] % k
            remainder_freq[r] = remainder_freq.get(r, 0) + 1

        for j in range(i + 1, len(nums) - 1):
            needed = (k - (nums[i] + nums[j]) % k) % k
            count += remainder_freq.get(needed, 0)

            remainder_freq[nums[j+1] % k] -= 1

    return count


print(count_triplets([1,2,3,4,5], 3))      # Expected: 4
print(count_triplets([3,3,3], 3))           # Expected: 1
print(count_triplets([1,2,3,4,5,6], 6))    # Expected: 4
print(count_triplets([2,2,2,2], 2))         # Expected: 4
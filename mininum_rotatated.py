

def find_min(nums):
    def binarySearch(left, right):
        if right - left <= 1:
            return min(nums[left], nums[right])
        
        middle = (right + left) // 2
        
        if nums[middle] > nums[middle + 1]:
            return binarySearch(middle, right)
        else:
            return binarySearch(left, middle)

    return binarySearch(0, len(nums) - 1)



print(find_min([3, 4, 5, 1, 2]))        # Expected: 1
print(find_min([4, 5, 6, 7, 0, 1, 2]))  # Expected: 0
print(find_min([11, 13, 15, 17]))       # Expected: 11
print(find_min([2, 1]))                 # Expected: 1
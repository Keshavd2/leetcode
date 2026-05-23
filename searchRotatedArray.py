def search(nums, target):
    if nums == []:
        return -1
    
    left, right = 0, len(nums) - 1
    middle = (left + right) // 2

    while(True):
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        
        if left == right:
            break
        
        if target >= nums[left] and target <= nums[middle]:
            right = middle
        elif target > nums[middle] and target <= nums[right]:
            left = middle
        elif target < nums[left]:
            left = middle
        elif target > nums[right]:
            right = middle
        
        middle = (left + right) // 2
            
    return -1


print(search([4,5,6,7,0,1,2], 0))
print(search([4,5,6,7,0,1,2], 3))
print(search([1,3], 3))
print(search([3,1], 1))
print(search([2], 2))
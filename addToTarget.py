def addToTarget (nums, target):
    recents = {}

    for i, num in enumerate(nums):
        difference = target - num
        if difference in recents:
            return [recents[difference], i]
        else:
            recents[num] = i

numm = [2,7,8,10]
print(addToTarget(numm, 9))
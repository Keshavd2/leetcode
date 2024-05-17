class Solution:
    def canJump(self, nums) -> bool:
        lastIndex = len(nums) - 1
        return Solution.FindPath(self, nums, lastIndex, 0)

    def FindPath(self, nums, lastIndex, currentIndex):
        if currentIndex == lastIndex:
            return True

        for jump in range(1, nums[currentIndex] + 1):
            pathExist = (Solution.FindPath(self, nums, lastIndex, currentIndex + jump))
            if pathExist:
                return True

        return False



problem = Solution()
print(problem.canJump([2,3,1,0,4]))
import math
class Solution:
    def threeSum(self, nums):
        ans = []
        sets = []
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if {nums[i], nums[j], nums[k]} in sets:
                            continue
                        ans.append([nums[i], nums[j], nums[k]])
                        sets.append({nums[i], nums[j], nums[k]})

        return ans



answer = Solution()
print(answer.threeSum([-1,0,1,2,-1,-4]))
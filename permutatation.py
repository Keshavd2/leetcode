class Solution:
    output = []
    counter = 0
    def permute(self, nums: List[int]) -> List[List[int]]:
        num_permutations = 1
        for i in range(0,len(nums)):
            num_permutations *= len(nums) - i

        print(self.output)

        result = Solution.recur(self,[],nums, [], num_permutations, self.output)
        print(self.output)
        return self.output

    def recur(self,used,nums, a_permutation, number, out):
        if len(a_permutation) == len(nums):
            print(a_permutation)
            out.append(a_permutation)
        else:
            for num in nums:
                if num in used:
                    continue 
                used.append(num)
                a_permutation.append(num)
                Solution.recur(self,used,nums, a_permutation, number, out)
                used.remove(num)
                a_permutation.remove(num)
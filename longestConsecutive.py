class Solution:
    def longestConsecutive(self, nums):
        if nums == []:
            return 0

        list_of_positive_num_sets = []
        list_of_negative_num_sets = []
        last_consecutive_num = {}
    
        for i in range(0,len(nums)):
            if nums[i] >= 0:
                list_of_positive_num_sets.append(set())
            else:
                list_of_negative_num_sets.append(set())
        
        while len(list_of_positive_num_sets) in nums:
            list_of_positive_num_sets.append(set())
        while -1 * len(list_of_negative_num_sets) in nums:
            list_of_negative_num_sets.append(set())

        for num in nums:
            if num >= 0:
                list_of_positive_num_sets[(num % (len(list_of_positive_num_sets)))].add(num)
            else:
                list_of_negative_num_sets[abs(num) % (len(list_of_negative_num_sets))].add(num)
            list_of_negative_num_sets.reverse()

        for a_set in list_of_negative_num_sets + list_of_positive_num_sets:
            if last_consecutive_num == {}:
                for num in a_set:
                    last_consecutive_num[num] = 1
                continue
            else:
                for num in a_set:
                    check_this_num = num - 1
                    if check_this_num not in last_consecutive_num.keys():
                        last_consecutive_num[num] = 1
                    else:
                        count = last_consecutive_num[check_this_num]
                        last_consecutive_num.pop(check_this_num)
                        last_consecutive_num[num] = count + 1
                
            
        print(last_consecutive_num)
        return max(last_consecutive_num.values())



answer = Solution()
answer.longestConsecutive([100,4,101,1,3,2])
answer.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
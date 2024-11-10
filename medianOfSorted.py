class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        new_list = []

        if m > 0 and n > 0:
            if nums1[0] >= nums2[n - 1]:
                new_list = nums2 + nums1
            elif nums1[m - 1] <= nums2[0]:
                new_list = nums1 + nums2
            
        else:
            new_list = nums1 + nums2
        
        if new_list == []:
            return []
        
        if (m + n) % 2 == 0:
            return (new_list[((m + n) / 2) - 1] + new_list[((m + n) / 2)]) / 2.0
        else:
            return new_list[((m + n) / 2)]
                

answer = Solution()
b = answer.findMedianSortedArrays([1,3], [2])
print(b)
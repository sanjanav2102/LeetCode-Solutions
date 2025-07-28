class Solution(object):
    def pivotIndex(self, nums):
        left = 0
        tot = sum(nums)
        flag = 0
        for i in range(len(nums)):
            right = tot - nums[i] - left
            if left == right:
                flag = 1
                return i
            else:
                left += nums[i]
        if flag == 0:
            return -1
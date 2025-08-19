class Solution(object):
    def maxSubArray(self, nums):
        res = nums[0]
        ends = nums[0] 
        for i in range(1,len(nums)):
            ends = max(ends+nums[i],nums[i])
            res = max(ends,res)
        return res
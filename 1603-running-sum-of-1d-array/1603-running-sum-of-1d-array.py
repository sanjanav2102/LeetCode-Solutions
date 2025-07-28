class Solution(object):
    def runningSum(self, nums):
        ans = [0]*len(nums)
        prev = ans[0]
        ans[0] = nums[0]
        for i in range(1,len(nums)):
            ans[i] = nums[i]+ans[i-1]
        return ans

        
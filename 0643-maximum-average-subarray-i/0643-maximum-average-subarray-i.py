class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        w_sum = 0
        for i in range(0,k):
            w_sum+=nums[i]
        max_result = w_sum
        for i in range(k,len(nums)):
            w_sum+=nums[i]-nums[i-k]
            max_result = max(max_result,w_sum)
        return float(max_result)/k

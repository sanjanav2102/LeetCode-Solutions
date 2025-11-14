class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            # Expand window
            curr_sum += num

            # Update global maximum
            max_sum = max(max_sum, curr_sum)

            # Shrink/reset window when it becomes harmful
            if curr_sum < 0:
                curr_sum = 0   # drop window completely

        return max_sum
        
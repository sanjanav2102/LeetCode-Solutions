class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        curr_sum = 0
        min_len = float('inf')

        for r in range(len(nums)):
            curr_sum += nums[r]  # expand window

            # shrink window while condition satisfied
            while curr_sum >= target:
                min_len = min(min_len, r - l + 1)
                curr_sum -= nums[l]  # shrink from left
                l += 1

        return 0 if min_len == float('inf') else min_len

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = set()           # to track distinct elements in the current window
        w_sum = 0              # current window sum
        max_sum = 0
        left = 0

        for right in range(len(nums)):
            # If duplicate found, shrink window from the left
            while nums[right] in seen:
                seen.remove(nums[left])
                w_sum -= nums[left]
                left += 1

            # Add new element to window
            seen.add(nums[right])
            w_sum += nums[right]

            # Maintain window size == k
            if right - left + 1 > k:
                seen.remove(nums[left])
                w_sum -= nums[left]
                left += 1

            # If valid window of size k, update answer
            if right - left + 1 == k:
                max_sum = max(max_sum, w_sum)

        return max_sum

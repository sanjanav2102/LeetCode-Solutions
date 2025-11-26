class Solution(object):
    def findPeakElement(self, nums):
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < nums[mid + 1]:
                # peak is on the right side
                l = mid + 1
            else:
                # peak is on the left side (including mid)
                r = mid

        # left == right → peak index
        return l

'''class Solution(object):
    def findPeakElement(self, nums):
        l = 0
        for h in range(1,len(nums)):
            if nums[h-1] <= nums[h]:
               # l+=1
               h+=1
               if h == len(nums):
                return h-1    
            else:
                return h-1
        else:
            return 0'''

        
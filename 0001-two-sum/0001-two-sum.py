class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            x = nums[i]
            value = target - x
            if value in nums :
                if i != nums.index(value):
                    return [i,nums.index(value)]

        
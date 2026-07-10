class Solution(object):
    def reverse(self,nums,start,end):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1
        return nums
    def rotate(self, nums, k):
        n = len(nums)
        k = k%n
        if k==0 or n == 0:
            return nums
        else:
            nums = self.reverse(nums,0,n-1)
            nums = self.reverse(nums,0,k-1)
            nums = self.reverse(nums,k,n-1)
            return nums
class Solution(object):
    def threeSum(self, nums):
        ans = []
        nums.sort()
        for i in range(0,len(nums)):
            j=i+1
            k = len(nums)-1
            x = nums[i]
            val = 0-x
            while(j<k and k<len(nums)):
                
                if (nums[j]+nums[k] < val):
                    j+=1
                elif (nums[j]+nums[k] > val):
                    k-=1
                else:
                    l=[nums[i],nums[j],nums[k]]
                    if l not in ans:
                        ans.append(l)
                    j+=1
                    k-=1
        return ans 
           



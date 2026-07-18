class Solution(object):
    def intersection(self, nums1, nums2):
        ans = []
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        n,m = len(nums1),len(nums2)
        while i<n and j<m:
            if nums1[i] == nums2[j]:
                if not ans or ans[-1] != nums1[i]:
                    ans.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1
        return ans
        
            
        
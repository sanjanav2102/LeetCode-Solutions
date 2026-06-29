class Solution(object):
    def getCommon(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        i,j = 0,0
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1
        else:
            return -1


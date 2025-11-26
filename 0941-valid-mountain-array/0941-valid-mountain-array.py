class Solution(object):
    def validMountainArray(self, arr):
        n = len(arr)
        if n < 3:
            return False

        # step 1: find the peak
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # peak cannot be first or last
        if i == 0 or i == n - 1:
            return False

        # step 2: walk down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        # if we reached the end → valid mountain
        return i == n - 1

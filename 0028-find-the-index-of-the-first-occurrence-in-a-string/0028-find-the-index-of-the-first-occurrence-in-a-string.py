class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:  # Handle the edge case where needle is empty
            return 0
        
        n, m = len(haystack), len(needle)  # Lengths of haystack and needle
        for i in range(n - m + 1):  # Iterate only until the last possible start index
            if haystack[i:i + m] == needle:  # Compare substring of length `m`
                return i
        
        return -1  # Return -1 if no match is found

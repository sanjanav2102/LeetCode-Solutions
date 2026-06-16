class Solution(object):
    def reverseBits(self, n):
        # '032b' automatically creates a 32-bit binary string with zeros
        s_rev = format(n, '032b')[::-1]
        return int(s_rev, 2)

class Solution(object):
    def countSubstrings(self, s):
        count = 0
        n = len(s)

        def expand(left, right):
            c = 0
            while left >= 0 and right < n and s[left] == s[right]:
                c += 1
                left -= 1
                right += 1
            return c

        for i in range(n):
            # Odd-length palindromes
            count += expand(i, i)

            # Even-length palindromes
            count += expand(i, i + 1)

        return count
class Solution(object):
    def reverseVowels(self, s):
        l = 0
        s = list(s)
        r = len(s) - 1

        vow = "aeiouAEIOU"

        while l < r:
            if s[l] in vow and s[r] in vow:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

            elif s[l] in vow and s[r] not in vow:
                r -= 1

            elif s[r] in vow and s[l] not in vow:
                l += 1

            else:
                l += 1
                r -= 1

        ans = "".join(s)
        return ans
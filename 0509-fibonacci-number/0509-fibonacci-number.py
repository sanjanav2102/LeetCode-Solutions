class Solution(object):
    def fib(self, n):
        dp = [-1]*(n+1)
        if n<= 1:
            return n
        if dp[n] != -1:
            return dp[n]
        else:
            dp[n] = self.fib(n-1)+self.fib(n-2)
        return dp[n]

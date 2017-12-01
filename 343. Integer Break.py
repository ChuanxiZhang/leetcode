class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(dp[j],j) * max(dp[i - j], i - j))
        return dp[n]
                

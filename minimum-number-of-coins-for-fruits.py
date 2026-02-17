class Solution:
    def minimumCoins(self, prices) -> int:
        n = len(prices)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0 
        for i in range(n - 1, -1, -1):

            for j in range(i + 1, min(n, i + i + 2) + 1):
                dp[i] = min(dp[i], prices[i] + dp[j])
        
        return dp[0]
        

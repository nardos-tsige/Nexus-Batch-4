class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)
        dp[1] = 1  
        for day in range(1, n + 1):
    
            start_share = day + delay
            end_share = min(day + forget, n + 1)
            
            for share_day in range(start_share, end_share):
                if share_day <= n:
                    dp[share_day] = (dp[share_day] + dp[day]) % MOD
        
        total = 0
        for day in range(max(1, n - forget + 1), n + 1):
            total = (total + dp[day]) % MOD
            
        return total

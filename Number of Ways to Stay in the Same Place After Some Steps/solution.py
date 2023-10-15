class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        length = min(steps, arrLen)
        dp = [0] * length
        dp[0] = 1
        mod = 10 ** 9 + 7
        for step in range(1, steps + 1):
            next_dp = [0] * length
            for i in range(0, length):
                next_dp[i] += dp[i]
                if i > 0:
                    next_dp[i] = (next_dp[i] + dp[i - 1]) % mod
                if i < length - 1:
                    next_dp[i] = (next_dp[i] + dp[i + 1]) % mod
            dp = next_dp
        
        return dp[0]

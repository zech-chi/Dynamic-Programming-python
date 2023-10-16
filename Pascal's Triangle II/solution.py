class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]
        for _ in range(rowIndex):
            next_dp = [0] * (len(dp) + 1)
            next_dp[0] = 1
            next_dp[-1] = 1
            for i in range(1, len(dp)):
                next_dp[i] = dp[i - 1] + dp[i]
            dp = next_dp

        return dp

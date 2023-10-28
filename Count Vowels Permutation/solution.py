class Solution:
    def countVowelPermutation(self, n: int) -> int:
        '''
        {
            'a': {'e'},
            'e': {'a', 'i'},
            'i': {'a', 'e', 'o', 'u'},
            'o': {'i', 'u'},
            'u': {'a'}
        }

                ['a', 'e', 'i', 'o', 'u']
        n = 1      1    1    1    1    1
        n = 2      1    2    4    2    1
        n = 3      2    5    6    5    1
        n = 4      5    8   13    7    2
        '''
        dp = [1] * 5
        for _ in range(n - 1):
            next_dp = [0] * 5
            next_dp[0] = dp[1]
            next_dp[1] = dp[0] + dp[2]
            next_dp[2] = dp[0] + dp[1] + dp[3] + dp[4]
            next_dp[3] = dp[2] + dp[4]
            next_dp[4] = dp[0]

            dp = next_dp

        return sum(dp) % (10 ** 9 + 7)

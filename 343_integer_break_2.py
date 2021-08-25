class Solution:
    # Below is the bottom-up approach,
    def integerBreak(self, n: int) -> int:
        dp = [None for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 0
        for index in range(2, n + 1):
            max_value = float('-inf')
            for subtract_amt in range(1, index):
                difference = index - subtract_amt
                curr_value = subtract_amt * max(difference, dp[difference])
                max_value = max(curr_value, max_value)
            dp[index] = max_value
        return dp[n]


if __name__ == '__main__':
    n = 10
    solution_instance = Solution()
    solution_to_return = solution_instance.integerBreak(n)
    print(solution_to_return)

class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [1] + [0 for i in range(amount)]
        for coin in coins:
            # We need to update the dp array only starting from coin's value
            for amount_to_update in range(coin, len(dp)):
                dp[amount_to_update] += dp[amount_to_update - coin]
        return dp[amount]


if __name__ == '__main__':
    test_amount = 5
    test_coins = [1, 2, 5]
    solution_instance = Solution()
    print(solution_instance.change(test_amount, test_coins))

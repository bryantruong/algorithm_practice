class Solution:
    def coinChange(self, coins, amount) -> int:
        """
        Top-Down recursive approach to 322. Coin Change
        :param coins: List of integers
        :param amount: integer
        :return: the fewest number of coins needed to make up the amount, or -1 if it isn't possible.
        """
        # Exceptional case
        if amount == 0:
            return 0
        # DP List. Each index corresponds to amount. Ex: num_of_coins[3] represents number of coins needed for amount 3
        num_of_coins = [float('inf')] * (amount + 1)
        # We know that it will always take 0 coins to get to an amount of 0.
        num_of_coins[0] = 0

        def get_num_of_coins(curr_amount):
            """
            Helper recursive function. Adjusts num_of_coins dp list as well.
            :param curr_amount:
            :return: Returns the lowest number of coins needed to arrive at curr_amount
            """
            # Try each possible denomination and save the positive ones
            possible_amounts = []
            for denomination in coins:
                change = curr_amount - denomination
                if change < 0:
                    continue
                if num_of_coins[change] < float('inf'):
                    potential_amount = num_of_coins[change]
                else:
                    potential_amount = get_num_of_coins(change)
                if potential_amount >= 0:
                    possible_amounts.append(potential_amount + 1)
            if possible_amounts:
                num_of_coins[curr_amount] = min(possible_amounts)
            # If there are no possible amounts, store -1 in the dp array
            else:
                num_of_coins[curr_amount] = -1
            return num_of_coins[curr_amount]

        return get_num_of_coins(amount)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    solution_instance = Solution()
    print(solution_instance.coinChange(coins, amount))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

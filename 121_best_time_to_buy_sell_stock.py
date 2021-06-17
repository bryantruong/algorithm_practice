# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 1:
            return 0
        curr_min = prices[0]
        best_profit = 0

        # loop starting from the second index (index 1)
        for i in range(1, len(prices)):
            if prices[i] < curr_min:
                # If we have a new min, update it accordingly
                curr_min = prices[i]
            else:
                profit = prices[i] - curr_min
                if profit > best_profit:
                    best_profit = profit
        return best_profit


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_case = [1, 1, 1]
    solution_instance = Solution()
    print(solution_instance.maxProfit(test_case))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

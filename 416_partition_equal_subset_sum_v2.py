# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Most optimal, 1-D approach
class Solution:
    # Capacity of Knapsack: Half the sum of the given array.
    # Objective: Achieve a total sum exact as the capacity.
    """
    If the total sum is odd, it is impossible.
    Get the capacity of our "knapsack". If we are able to have our knapsack reach exactly total sum/2, return true.
    Otherwise, return false.
    Before, our DP[i] represented the max value if our knapsack had the max possible capacity i.
    Now, our DP[i] can represent if it is possible to have the knapsack reach exactly i.
    So create a dp array from 0 to capacity.
    Ex: nums = [1,5,5,11]
    The target here is 11.
    For each number, we want to consider from i = 0 to i = 11, but in reverse, so that we don't double count.
    i = 0   1      2       3        4   5       6       7       8   9       10      11
    [False, False, False, False, False, False, False, False, False, False, False, False]
    At each index, we want to check if it is possible to get to the current i - current num or if i - num = 0
    for num = 1, they
     i = 0   1      2       3      4    5       6       7       8   9       10      11
    [False, True, False, False, False, False, False, False, False, False, False, False]

    for num = 5
    i = 0   1      2       3      4     5      6       7       8   9       10      11
    [False, True, False, False, False, True, True, False, False, False, False, False]

    for num = 5
    i = 0   1      2       3      4     5      6       7      8    9       10    11
    [False, True, False, False, False, True, True, False, False, False, False, True]

    At any point if dp[capacity] == true: return true.

    Space complexity: O(Capacity). Time Complexity: O(N * Capacity)
    For each number iterate for number <= indices <= capacity
    """

    def canPartition(self, nums) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        dp = [False for _ in range(target + 1)]
        for index, num in enumerate(nums):
            # Edge case, to avoid index out of bounds exceptions
            if num > target:
                continue
            # Have to go in reverse to prevent double countingf
            for cur_target in range(target, num - 1, -1):
                if dp[cur_target - num] or cur_target - num == 0:
                    dp[cur_target] = True
                # At any point, if dp[target] is True, return True to save time.
                if dp[target]:
                    return True
        return dp[target]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_nums = [1, 5, 5, 11]
    solution_instance = Solution()
    print(solution_instance.canPartition(test_nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

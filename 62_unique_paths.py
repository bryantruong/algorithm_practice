# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # First, build the empty DP matrix according to the dimensions
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # Initialize the first cell as 1
        dp[0][0] = 1
        # Iterate through the 2-d matrix in row-major order
        for row_index in range(m):
            for col_index in range(n):
                if row_index == 0 and col_index == 0:
                    dp[row_index][col_index] == 1
                    continue
                # Check the left neighbor of the current cell
                # Don't need to check the upper bound, since the for loop specifies the range
                if 0 <= col_index - 1:
                    dp[row_index][col_index] += dp[row_index][col_index - 1]
                # Check the upper neighbor of the current cell
                if 0 <= row_index - 1:
                    dp[row_index][col_index] += dp[row_index-1][col_index]
        return dp[m - 1][n-1]




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_m = 3
    test_n = 7
    solution_instance = Solution()
    print(solution_instance.uniquePaths(test_m, test_n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

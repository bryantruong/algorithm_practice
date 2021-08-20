def get_counts(string_number):
    zero_count, ones_count = 0, 0
    for char in string_number:
        if int(char) == 0:
            zero_count += 1
        else:
            ones_count += 1
    return zero_count, ones_count


class Solution:
    # Top-down solution w/memoization. Not as fast as bottom-up/iterative solution
    # def findMaxForm(self, strs, m: int, n: int) -> int:
    #     # Memoization dictionary.
    #     memo_dict = {}
    #     def try_subset(curr_index, zeros_left, ones_left):
    #         # The base case, when we have no option to add anything.
    #         if curr_index >= len(strs):
    #             return 0
    #         if (curr_index, zeros_left, ones_left) in memo_dict:
    #             return memo_dict[(curr_index, zeros_left, ones_left)]
    #         else:
    #             curr_str = strs[curr_index]
    #             zeros, ones = get_counts(curr_str)
    #             adding_result = float("-inf")
    #             # Try adding this current string to the subset
    #             if zeros <= zeros_left and ones <= ones_left:
    #                 # Since we are adding the element, add one as we unwind.
    #                 adding_result = try_subset(curr_index + 1, zeros_left - zeros, ones_left - ones) + 1
    #             skip_result = try_subset(curr_index + 1, zeros_left, ones_left)
    #             memo_dict[(curr_index, zeros_left, ones_left)] = max(skip_result, adding_result)
    #             return memo_dict[(curr_index, zeros_left, ones_left)]
    #
    #     return try_subset(0, m, n)

    # Dynamic programming solution. We have to fill it in in a top-down fashion, since
    # "each string will require us to iterate through the entirety of dp looking for data to update"
    # Return the last value: dp[m][n], where m is the number of zeros, n is the number of ones allowed
    def findMaxForm(self, S, M, N) -> int:
        # Each row represents the possible one's, each col represents the possible zero's
        dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
        for str in S:
            zeros = str.count("0")
            ones = len(str) - zeros
            # Start from M (The maximum number of zero's possible) for rows to the number of zeros present
            for i in range(M, zeros - 1, -1):
                # Start from N (The maximum number of one's possible) for rows to the number of ones present
                for j in range(N, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[M][N]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_strs = ["10", "0", "1"]
    test_m = 1
    test_n = 1
    solution_instance = Solution()
    print(solution_instance.findMaxForm(test_strs, test_m, test_n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

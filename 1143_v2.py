class Solution:
    """
    This is the top-down solution. See 1143_v2 for the bottom-up tabulation approach.
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp_matrix[i][j] represents the longest common subsequence for text1[i:] and text2[j:]
        dp_matrix = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        # Start from the back, since we want to build up our solution.
        # Skip the last row an col, since those are base cases
        for index_1 in range(len(text1) - 1, -1, -1):
            for index_2 in range(len(text2) - 1, -1, -1):
                if text1[index_1] == text2[index_2]:
                    dp_matrix[index_1][index_2] = 1 + dp_matrix[index_1 + 1][index_2 + 1]
                else:
                    dp_matrix[index_1][index_2] = max(dp_matrix[index_1 + 1][index_2], dp_matrix[index_1][index_2 + 1])

        return dp_matrix[0][0]


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestCommonSubsequence("abcd", "bd"))

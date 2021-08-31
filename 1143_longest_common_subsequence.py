class Solution:
    """
    This is the top-down solution. See 1143_v2 for the bottom-up tabulation approach.
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo_dict = {}

        def recursive_get_subsequence(index_1, index_2):
            id = (index_1, index_2)
            # Consult the memoization dict
            if id in memo_dict:
                return memo_dict[id]
            # If one of the two strings are empty, there is nothing in common.
            if index_1 >= len(text1) or index_2 >= len(text2):
                memo_dict[id] = 0
                return 0
            # We can now assume that both are nonnull
            if text1[index_1] == text2[index_2]:
                memo_dict[id] = 1 + recursive_get_subsequence(index_1 + 1, index_2 + 1)
                return memo_dict[id]
            else:
                # We have two options: Skip the current char for text1, or skip current char for text2
                memo_dict[id] = max(recursive_get_subsequence(index_1, index_2 + 1),
                                    recursive_get_subsequence(index_1 + 1, index_2))
            return memo_dict[id]

        return recursive_get_subsequence(0, 0)

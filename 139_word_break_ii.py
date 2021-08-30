class Solution:
    """
    Brute Force Solution: TLE
    Below is the bottom-up iterative solution.
    """

    def wordBreak(self, s: str, wordDict) -> bool:
        """
        Initialize an array of length s for tabulation.
        dp[i] means that it is possible to make word s[0:i+1] from words in wordDict.
        How do we use the dp table? Look at elements in dp table before it. if it is true, see if the string from
        the element before to the current element is in the dictionary. if so, mark current spot as true.
              c a t s a n d o g
        i = 0 1 2 3 4 5 6 7 8 9
         [ T,F,F,T,T,

        In essence, we need to check if every element before is true and if the rest of the string after that
        element is in the wordDict.
        :param s:
        :param wordDict:
        :return: The last value in the array.
        """
        dict_set = set(wordDict)
        dp = [None for _ in range(len(s) + 1)]
        # Base case. We can always make an empty string.
        dp[0] = True

        for outer_i in range(1, len(s) + 1):
            for inner_i in range(outer_i):
                # See if there's any way to build off of previous tabulations (via inner_i) to solve for outer_i
                if dp[inner_i] and s[inner_i:outer_i] in dict_set:
                    dp[outer_i] = True
                    # Once we find out it is possible, we don't need to keep trying other combinations
                    break
            if not dp[outer_i]:
                dp[outer_i] = False
        return dp[len(s)]


if __name__ == '__main__':
    solution_instance = Solution()
    s = "catsanddog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(solution_instance.wordBreak(s, wordDict))

class Solution:
    """
    Brute Force Solution: TLE
    Below is the top-down recursive w/memoization.
    """

    def wordBreak(self, s: str, wordDict) -> bool:
        def assemble_word(string_remaining):
            """
            Recursive helper to see if we can use words from word_dict to match string_remaining
            :param string_remaining: the string that we have to try to assemble by using words from wordDict
            :return: Boolean, if it is possible
            """
            # See if we have already calculated this
            if string_remaining in dp_dict:
                return dp_dict[string_remaining]
            # If we don't have any string remaining, we were successful.
            if not string_remaining:
                return True
            # See what possible prefixes we can remove
            prefix = ""
            for prefix_end in range(0, len(string_remaining)):
                prefix = prefix + string_remaining[prefix_end]
                if prefix in word_set:
                    # See if the rest of the string is valid via recursion.
                    if assemble_word(string_remaining[prefix_end + 1:]):
                        dp_dict[prefix] = True
                        return True
            dp_dict[prefix] = False
            return False

        # Cast the wordDict to a set for faster lookup time. O(N)
        word_set = set(wordDict)
        dp_dict = {}
        return assemble_word(s)


if __name__ == '__main__':
    solution_instance = Solution()
    s = "applepenapple"
    wordDict = ["apple","pen"]
    print(solution_instance.wordBreak(s, wordDict))

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from collections import deque

# This was a very unsuccessful problem for me. Had to just copy and paste someone else's solution b/c of TLE's.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        for i in range(len(s)):
            # For odd lengths
            l, r = i, i
            while l >= 0 and r< len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l: r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            # For even lengths
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                # Expand outwards
                l -= 1
                r += 1
        return res



    # #### REIMPLEMENTED A DP SOLUTION. O(N^2) COMPLEXITY. STILL GO TTLE
    # def longestPalindrome(self, s: str) -> str:
    #     dp = [[None for i in range(len(s))] for j in range(len(s))]
    #     diff = 0
    #     best_pal = ""
    #     # Iterate through each pair by difference between start and stop
    #     # EX: does (0,0), (1,1)... then does (0,1), (1,2)... then (0,2), (1,3), etc.
    #     while diff < len(s):
    #         start = 0
    #         stop = start + diff
    #         while stop <= len(s) - 1:
    #             # Special cases for strings with length 1 and 2
    #             if diff <= 1:
    #                 # For strings with length 1, they are always palindromes
    #                 if start == stop:
    #                     # Start index will be represented by the rows, Stop by columns
    #                     dp[start][stop] = True
    #                     if len(best_pal) < len(s[start:stop + 1]):
    #                         best_pal = s[start:stop + 1]
    #                 # For two letter palindromes
    #                 if s[start] != s[stop]:
    #                     dp[start][stop] = False
    #                 else:
    #                     dp[start][stop] = True
    #                     if len(best_pal) < len(s[start:stop + 1]):
    #                         best_pal = s[start:stop + 1]
    #             else:
    #                 if s[start] != s[stop]:
    #                     dp[start][stop] = False
    #                 else:
    #                     # Rely on the previously computed values
    #                     if dp[start + 1][stop - 1]:
    #                         if len(best_pal) < len(s[start:stop + 1]):
    #                             best_pal = s[start:stop + 1]
    #                         dp[start][stop] = True
    #                     else:
    #                         dp[start][stop] = False
    #             start += 1
    #             stop += 1
    #         diff += 1
    #     return best_pal

####### BELOW WAS MY SOLUTION BUT GOT TLE. ######
# def __init__(self):
#     self.palindromes = {}
#
# def longestPalindrome(self, s: str) -> str:
#     max_pal = ""
#     for start, char in enumerate(s):
#         for stop in range(start + 1, len(s) + 1):
#             if self.is_palindrome(s[start:stop]):
#                 if (stop - start) > len(max_pal):
#                     max_pal = s[start:stop]
#     return max_pal
#
# def is_palindrome(self, word):
#     if word in self.palindromes:
#         return self.palindromes[word]
#     # Check if first letter == last letter
#     if word[0] != word[-1]:
#         self.palindromes[word] = False
#         return False
#     if len(word) <= 3:
#         self.palindromes[word] = True
#         return True
#     else:
#         # Make sure that middle of the word is a palindrome
#         if self.is_palindrome(word[1:-1]):
#             self.palindromes[word] = True
#             return True
#         else:
#             self.palindromes[word] = False
#             return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "cbbd"
    solution_instance = Solution()
    print(solution_instance.longestPalindrome(s))

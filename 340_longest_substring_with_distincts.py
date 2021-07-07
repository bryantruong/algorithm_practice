class Solution:
    # Begin the actual solution
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        last_seen_dict = {}  # Stores the mapping between letter to last seen index
        start = end = 0
        best_size = 0
        while end < len(s):
            if s[end] in last_seen_dict:
                # Have to remove it, since order is maintained on initial insertion (not updates)
                last_seen_dict.pop(s[end])
            last_seen_dict[s[end]] = end
            if len(last_seen_dict) > k:
                earliest_char = list(last_seen_dict.items())[0][0]  # Since dictionaries are ordered in Python 3.6+
                start = last_seen_dict[earliest_char] + 1  # Adjust the start of the window
                last_seen_dict.pop(earliest_char)
            best_size = max((end - start + 1), best_size)
            end += 1
        return best_size

    # My solution. Very slow.
    # def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    #     if len(s) <= k:
    #         return len(s)
    #     if k == 0:
    #         return 0
    #     curr_str = ""
    #     num_distinct = best_len = end = 0
    #     while end != len(s):
    #         if s[end] not in curr_str:
    #             num_distinct += 1
    #             if num_distinct > k:
    #                 curr_str = self.move_window(self, curr_str, k)
    #                 # Because we'll be adding the new letter to the current string no matter what
    #                 num_distinct = k
    #         curr_str += s[end]
    #         end += 1
    #         if len(curr_str) > best_len:
    #             best_len = len(curr_str)
    #     return best_len
    #
    # @staticmethod
    # def move_window(self, curr_str, k):
    #     while len(set(curr_str)) > k - 1 and curr_str:
    #         # Advance the window
    #         curr_str = curr_str[1:]
    #     return curr_str


if __name__ == '__main__':
    test_case = "eceba"
    test_k = 2
    solution_instance = Solution()
    print(solution_instance.lengthOfLongestSubstringKDistinct(test_case, test_k))

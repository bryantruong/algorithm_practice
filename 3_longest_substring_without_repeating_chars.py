# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Store the last seen index of each char in this dictionary
        chars_to_index = {}
        current_start = 0
        max_length = 0
        for index, char in enumerate(s):
            # First, check if we have seen this character before
            if char in chars_to_index:
                last_seen_i = chars_to_index[char]
                if current_start <= last_seen_i + 1:
                    # Trim the current substring
                    current_start = last_seen_i + 1
                chars_to_index[char] = index
            else:
                # This is a new character that we have encountered
                chars_to_index[char] = index

            max_length = max(max_length, (index - current_start) + 1)
        return max_length


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution_obj = Solution()
    print(solution_obj.lengthOfLongestSubstring("tmmzuxt"))

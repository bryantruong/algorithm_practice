from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_counts = defaultdict(int)
        left = 0
        longest = 0
        for right in range(len(s)):
            window_counts[s[right]] += 1

            # If the window is invalid, slide the left inwards
            if (right - left + 1) - max(window_counts.values()) > k:
                window_counts[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest

from collections import deque


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # The approach is to ONLY compare once we find a char that won't be deleted
        s_pointer = len(s) - 1
        t_pointer = len(t) - 1

        # Keep track of the number of backspaces to account for
        s_to_skip = 0
        t_to_skip = 0
        while s_pointer >= 0 or t_pointer >= 0:
            # First, get the s pointer into position (or until we reach end of s)
            while s_pointer >= 0:
                if s[s_pointer] == "#":
                    s_to_skip += 1
                    s_pointer -= 1
                else:
                    # This means we found a non-backspace char, but we have to skip it
                    if s_to_skip > 0:
                        s_to_skip -= 1  # Mark it as skipped
                        s_pointer -= 1
                    else:
                        # We found a char that won't be deleted
                        break

            # Next, get the t pointer in position
            # First, get the t pointer into position (or until we reach end of t)
            while t_pointer >= 0:
                if t[t_pointer] == "#":
                    t_to_skip += 1
                    t_pointer -= 1
                else:
                    # This means we found a non-backspace char, but we have to skip it
                    if t_to_skip > 0:
                        t_to_skip -= 1  # Mark it as skipped
                        t_pointer -= 1
                    else:
                        # We found a char that wno't be deleted
                        break

            # Both pointers should be at valid characters OR at the beginning of the string
            if (s_pointer < 0 and t_pointer >= 0) or (t_pointer < 0 and s_pointer >= 0):
                # If one word's pointer is finished and the other's isn't, they are unequal
                return False
            # If both are in-play and pointing to a char, compare them.
            if s_pointer >= 0 and t_pointer >= 0:
                if s[s_pointer] != t[t_pointer]:
                    return False
            # Move both indices in.
            s_pointer -= 1
            t_pointer -= 1
        # If both end at the same time, they are equal
        return True




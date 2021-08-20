from collections import deque


class Solution:
    """
    Examples:
    1. s = "3[a]2[bc]" -> aaabcbc
    2. s = "3[a2[c]]" -> accaccacc
    3. s = 2[a2[c]b2[a]d] -> accbaadaccbaad


    We can't assume that k is one digit!
    Iterate through the string. Add everything to the stack until current character is a closing bracket.
        - Pop off everything the stack until we reach an opening bracket. Everything we popped off prior will be string
         to repeat.
        - Continue to pop off until stack is empty or current char is no longer a number. This will be k.
        - Convert k to an integer. Reverse the string and add to the stack k times
    """
    def decodeString(self, s: str) -> str:
        stack = deque()
        for char in s:
            if char != ']':
                stack.append(char)
            # We have reached a closing bracket.
            else:
                # Pop off everything the stack until we reach an opening bracket.
                # Everything we popped off prior will be string to repeat.
                current_pop = stack.pop()
                string_to_repeat = ''
                while current_pop != '[':
                    # Add it to the string to repeat
                    string_to_repeat = string_to_repeat + current_pop
                    current_pop = stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    current_pop = stack.pop()
                    # Have to remember that we are working backwards here!
                    k = current_pop + k
                # Convert k into an integer form
                k = int(k)
                # Add string_to_repeat, in reverse, to the stack k times
                for _ in range(k):
                    for char_index in range(len(string_to_repeat) - 1, -1, -1):
                        stack.append(string_to_repeat[char_index])
        solution = ""
        for letter in stack:
            solution += letter
        return solution


if __name__ == '__main__':
    test_s = "100[leetcode]"
    solution_instance = Solution()
    print(solution_instance.decodeString(test_s))
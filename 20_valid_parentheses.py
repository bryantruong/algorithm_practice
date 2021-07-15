from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        visited_stack = deque()
        mappings = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for char in s:
            if char == '(' or char == '{' or char == '[':
                visited_stack.append(char)
            else:
                if not visited_stack or mappings[visited_stack[-1]] != char:
                    return False
                visited_stack.pop()
        if visited_stack:
            return False
        return True


if __name__ == '__main__':
    test_case = "([)]"
    solution_instance = Solution()
    print(solution_instance.isValid(test_case))

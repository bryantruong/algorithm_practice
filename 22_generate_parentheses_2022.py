from collections import deque
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solutions = []

        def generate_parentheses(num_open, curr_string, num_remaining):
            #  Base case:
            if num_remaining == 0:
                solutions.append(curr_string)
                return
            if num_open > 0:
                # We can try and close the parentheses we have
                generate_parentheses(num_open - 1, curr_string + ")", num_remaining - 1)
            # We can always try to open up more parentheses, as long as we don't already have n open
            if num_open < num_remaining:
                generate_parentheses(num_open + 1, curr_string + "(", num_remaining)
            return

        generate_parentheses(1, "(", n)
        return solutions


if __name__ == '__main__':
    test_case = 2
    solution_instance = Solution()
    print(solution_instance.generateParenthesis(test_case))

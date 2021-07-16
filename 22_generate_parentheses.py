from collections import deque


class Solution:
    def __init__(self):
        self.solution = []

    def generateParenthesis(self, n: int):
        self.recursiveAdd(1, "(", n)
        return self.solution

    def recursiveAdd(self, num_open, curr_string, pairs_left):
        if pairs_left == 0:
            self.solution.append(curr_string)
            return
        # We always want to attempt to append an open, and we always want to attempt to append a close.
        # BUT there are rules that dictate when it is valid.
        if num_open < pairs_left:
            # Open another pair. Pairs_left stays the same
            self.recursiveAdd(num_open + 1, curr_string + "(", pairs_left)
        if num_open > 0:
            # We can only close if there are open parentheses. Anytime we close, the number of pairs_left decreases
            self.recursiveAdd(num_open - 1, curr_string + ")", pairs_left - 1)
        return


if __name__ == '__main__':
    test_case = 3
    solution_instance = Solution()
    print(solution_instance.generateParenthesis(test_case))

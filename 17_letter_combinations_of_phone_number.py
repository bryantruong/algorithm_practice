class Solution:
    # Make this static, since these mappings are the same always.
    mappings = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def __init__(self):
        # These are instance variables
        self.solution_list = []

    def addPossibleLetters(self, current_string, digits_left):
        if not digits_left:
            self.solution_list.append(current_string)
            return
        for letter in self.mappings[digits_left[0]]:
            self.addPossibleLetters(current_string + letter, digits_left[1:])

    def letterCombinations(self, digits: str):
        if not digits:
            return self.solution_list
        self.addPossibleLetters("", digits)
        return self.solution_list


if __name__ == '__main__':
    test_digits = ""
    solution_instance = Solution()
    print(solution_instance.letterCombinations(test_digits))

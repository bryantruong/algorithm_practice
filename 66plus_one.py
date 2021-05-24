# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            curr_digit = digits[i]
            if curr_digit != 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    digits = [9,9,9,9]
    solution_instance = Solution()
    print(solution_instance.plusOne(digits))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

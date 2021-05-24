# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



class Solution:
    def __init__(self):
        self.dp_dict = {}

    def climbStairs(self, n: int) -> int:
        if n not in self.dp_dict:
            if n == 1:
                self.dp_dict[n] = 1
            elif n == 2:
                self.dp_dict[n] = 2
            else:
                self.dp_dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp_dict[n]
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    solution_instance = Solution()
    print(solution_instance.climbStairs(4))
    print(solution_instance.climbStairs(3))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

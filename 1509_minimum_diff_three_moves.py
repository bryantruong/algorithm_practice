# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def minDifference(self, nums) -> int:
        if len(nums) <= 4:
            return 0
        else:
            # Sort the list into ascending order, nlogn time complexity
            nums.sort()
            # Creates the pairs for the sliding window. We have four options. See the discussion solution here:
            # https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/discuss/730567/JavaC%2B%2BPython-Straight-Forward
            return min(b - a for a, b in zip(nums[:4], nums[-4:]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1, 5, 0, 10, 14]
    solution_instance = Solution()
    print(solution_instance.minDifference(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

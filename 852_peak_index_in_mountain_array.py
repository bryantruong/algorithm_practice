# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        left = 0
        right = len(arr) - 1
        while True:
            midpoint = (left + right) // 2
            if (arr[midpoint] > arr[midpoint + 1]) and (arr[midpoint] > arr[midpoint - 1]):
                return midpoint
            elif arr[midpoint - 1] < arr[midpoint] < arr[midpoint + 1]:
                # It is ascending, so look to the right
                left = midpoint + 1
            else:
                # It is descending, so look to the left
                right = midpoint
                # Note that we use floor division, so we can't use midpoint -1 when taking the left.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1, 20, 30, 14]
    solution_instance = Solution()
    print(solution_instance.peakIndexInMountainArray(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

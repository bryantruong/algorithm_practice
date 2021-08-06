class Solution:
    """
    We can see that with the simple implementation, it is worst case O(N), and is only faster than 40%.
    [5,7,7,8,8,10], target = 8
    Do binary search for left boundary:
    midpoint = 7 (index 2)
        7 < 8, so look at right
        midpoint = 8, (index 4)
        Condition: If midpoint >= target, look at left side
        8 == target. Look at left side, but include the midpoint
        Stop when array[start] == target
            midpoint = 8 (index 3)
            array[start] == target!
    Do the opposite for looking for right boundary.
    7 < 8, so look at right
        midpoint = 8 (index 4)
        if midpoint <= target, look at right side.
        Stop when array[stop] == target


[5, 7, 7, 8, 8, 10]
midpoint = 7, which is too small. look at the right side

[8, 8, 10]
midpoint = 8, which is equal to the target. look at the left side, though, since it is equal to the target
Takeaway. Look at left side if nums[midpoint' is greater than or equal to the target.
stop = midpoint
[8,8]
since stop == target, return target


    """

    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        left = self.find_left(nums, target)
        if left == -1:
            return [left, -1]
        else:
            return [left, self.find_right(nums, target)]

    def find_left(self, nums_array, target):
        # Finds the first position of the target (if it exists)
        result = -1
        start = 0
        stop = len(nums_array) - 1
        while start <= stop:
            midpoint = (start + stop) // 2
            if nums_array[midpoint] == target:
                # If the midpoint is the target, set the result, but continue to search the left side
                result = midpoint
                stop = midpoint - 1
            elif nums_array[midpoint] > target:
                stop = midpoint - 1
            else:
                start = midpoint + 1
        return result

    def find_right(self, nums_array, target):
        # Finds the last position of the target (if it exists)
        result = -1
        start = 0
        stop = len(nums_array) - 1
        while start <= stop:
            midpoint = (start + stop) // 2
            if nums_array[midpoint] == target:
                # If the midpoint is the target, set the result, but continue to search the right side
                result = midpoint
                start = midpoint + 1
            elif nums_array[midpoint] > target:
                stop = midpoint - 1
            else:
                start = midpoint + 1
        return result


if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    test_nums = [1, 2, 3, 3, 3, 3, 4, 5, 9]
    test_target = 3
    solution_instance = Solution()
    print(solution_instance.searchRange(test_nums, test_target))

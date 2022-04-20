from collections import deque


class Solution:
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        solution = deque()
        while left <= right:
            # If the right absolute value is greater
            if abs(nums[right]) >= abs(nums[left]):
                solution.appendleft(nums[right] ** 2)
                right -= 1  # Move the right pointer in by one
            else:
                # If the left absolute value is greater
                solution.appendleft(nums[left] ** 2)
                left += 1
        return solution

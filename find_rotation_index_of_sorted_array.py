class Solution:
    def find_rotation(self, nums):
        if len(nums) == 1:
            return 0
        return self.recursive_find_rotation(nums, 0, len(nums) - 1)

    # This problem is essentially the same as finding the minimum in a rotated sorted array, we just need the index
    def recursive_find_rotation(self, nums_array, start, stop):
        midpoint = (start + stop) // 2
        if nums_array[midpoint] <= nums_array[midpoint - 1]:
            return midpoint
        else:
            # See if the midpoint is in the left side, which is scrambled
            if nums_array[midpoint] < nums_array[start]:
                # If it is scrambled, we want to look at that side.
                return self.recursive_find_rotation(nums_array, start, midpoint)
            # See if the midpoint is in the right side, which is scrambled
            if nums_array[midpoint] > nums_array[stop]:
                return self.recursive_find_rotation(nums_array, midpoint + 1, stop)
            # Otherwise, the array wasn't even rotated
            return 0


if __name__ == '__main__':
    test_nums = [5, 1, 2, 3, 4]
    # Should return 3
    solution_instance = Solution()
    print(solution_instance.find_rotation(test_nums))

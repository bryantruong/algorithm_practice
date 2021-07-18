class Solution:
    def findMin(self, nums):
        start = 0
        stop = len(nums) - 1
        current_min = float('inf')
        while True:
            mid = (start + stop) // 2
            # The left side is normal
            if nums[mid] >= nums[start]:
                # See if the current minimum can be replaced
                if nums[start] < current_min:
                    current_min = nums[start]
                if nums[mid] <= nums[stop]:
                    # This means the right side is normal
                    return current_min
                else:
                    # Otherwise, we have to look at the right side, since it was rotated
                    start = mid + 1
            # The left side has been rotated
            else:
                # See if the current min can be replaced
                if nums[mid] < current_min:
                    current_min = nums[mid]
                    # Look at the left side, since it's been rotated
                    stop = mid - 1



if __name__ == '__main__':
    test_nums = [4, 6, 8, 10, 1]
    solution_instance = Solution()
    print(solution_instance.findMin(test_nums))

class Solution:
    def search(self, nums, target) -> int:
        start = 0
        stop = len(nums) - 1
        while start <= stop:
            midpoint = (start + stop) // 2
            if nums[midpoint] == target:
                return midpoint
            # First figure out which side (if any) has the rotated subarray
            if nums[midpoint] >= nums[start]:  # The left side is normal
                # Only take the left half if target is less than midpoint and is GTE the start of left half
                if nums[midpoint] > target >= nums[start]:
                    stop = midpoint - 1
                else:
                    start = midpoint + 1
            else:  # The right side is normal
                # Only take the right half if target is more than midpoint and is LTE the end of the right half
                if nums[midpoint] < target <= nums[stop]:
                    start = midpoint + 1
                else:
                    stop = midpoint - 1
        return -1


if __name__ == '__main__':
    test_nums = [4, 5, 6, 7, 0, 1, 2]
    test_target = 0
    solution_instance = Solution()
    print(solution_instance.search(test_nums, test_target))

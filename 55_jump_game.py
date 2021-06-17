class Solution:
    def canJump(self, nums):
        # Use this to store whether or not we have encountered a zero
        zero_index = None
        # Want to start iterating from the second to last element in the array
        for i in range(len(nums) - 2, -1, -1):
            # If we aren't looking to satisfy a zero yet, and we find a zero
            if not zero_index and nums[i] == 0:
                zero_index = i
            # It is nonzero and we are looking to satisfy a zero
            elif zero_index:
                dist_from_zero = abs(i - zero_index)
                if nums[i] > dist_from_zero:
                    zero_index = None
        # We never satisfied the zero we came across
        if zero_index is not None:
            return False
        # We either satisfied the zero or never came across one
        return True



if __name__ == '__main__':
    test_case = [1]
    solution_instance = Solution()
    print(solution_instance.canJump(test_case))

class Solution:
    def maxSubArray(self, nums) -> int:
        sums = [nums[0]]
        for i in range(1, len(nums)):
            # If the single value is greater than the accumulated sum
            if nums[i] > sums[i - 1] + nums[i]:
                sums.append(nums[i])
            else:
                # If the sum is greater than or equal to the accumulated sum, enter the sum
                sums.append(sums[i - 1] + nums[i])
        return max(sums)



if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    test_case = [8,-19,5,-4,20]
    solution_instance = Solution()
    print(solution_instance.maxSubArray(test_case))

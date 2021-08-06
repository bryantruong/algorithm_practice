class Solution:
    def maxProduct(self, nums) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        max_product = nums[0]
        # Start from the second value if possible
        for index in range(1, len(nums)):
            num = nums[index]
            previous_max_so_far = max_so_far
            max_so_far = max(num * min_so_far, num * max_so_far, num)
            min_so_far = min(num * min_so_far, num * previous_max_so_far, num)
            max_product = max(max_so_far, max_product)
        return max_product


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    test_case = [-4, -3, -2]
    solution_instance = Solution()
    print(solution_instance.maxProduct(test_case))

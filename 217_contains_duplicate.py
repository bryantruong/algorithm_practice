class Solution:
    def containsDuplicate(self, nums) -> bool:
        original_len = len(nums)
        new_len = len(set(nums))
        return not original_len == new_len

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    test_case = [1, 2, 3, 4, 2]
    solution_instance = Solution()
    print(solution_instance.containsDuplicate(test_case))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# This is the top-down recursive approach. Build up different sums from the starting index.
class Solution:
    def canPartition(self, nums) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        target_sum = total_sum // 2
        last_index = len(nums) - 1
        # Using a dictionary is easier and faster than the 2D List
        dp_dict = {}

        def make_subsums(curr_index, curr_sum) -> bool:
            if (curr_index, curr_sum) in dp_dict:
                return dp_dict[(curr_index, curr_sum)]
            if curr_sum == target_sum:
                dp_dict[(curr_index, curr_sum)] = True
                return True
            if curr_sum > target_sum:
                dp_dict[(curr_index, curr_sum)] = False
                return False
            if curr_index > last_index:
                return False
            # Try making a subset including the current index's value, as well as skipping it
            dp_dict[(curr_index, curr_sum)] = make_subsums(curr_index + 1, curr_sum + nums[curr_index]) or \
                                              make_subsums(curr_index + 1, curr_sum)
            return dp_dict[(curr_index, curr_sum)]

        return make_subsums(0, 0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_nums = [1, 5, 11, 5]
    solution_instance = Solution()
    print(solution_instance.canPartition(test_nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

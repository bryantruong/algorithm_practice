from typing import List


class Solution:
    def combinationSum3(self, target_length: int, target_val: int) -> List[List[int]]:
        sol = []

        def check_sums(curr_num, curr_sum, curr_path):
            # Base cases
            # When we failed to find a valid combination
            # We have to do > 10, since we always increment one when recursing down (even at the end)
            if curr_num > 10 or curr_sum > target_val:
                return
            if len(curr_path) == target_length:
                # We found a valid combination
                if curr_sum == target_val:
                    sol.append(curr_path.copy())
                return
            # Now, we have the two options: Use current value, or skip it.
            # Either way, we advance the current value, since we don't allow duplicates.
            # Using the current value
            curr_path.append(curr_num)
            check_sums(curr_num + 1, curr_sum + curr_num, curr_path)

            # Skipping it
            curr_path.pop()
            check_sums(curr_num + 1, curr_sum, curr_path)
            return

        check_sums(1, 0, [])
        return sol


if __name__ == '__main__':
    desired_length = 9
    desired_val = 45
    solution_instance = Solution()
    print(solution_instance.combinationSum3(desired_length, desired_val))

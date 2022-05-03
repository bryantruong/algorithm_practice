from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Emulating the NeetCode solution
        """
        solution = []

        def generate_combinations(curr_pos, curr_sum, curr_path):
            # Base cases
            if curr_sum == target:
                solution.append(curr_path.copy())
                return
            if curr_pos >= len(candidates) or curr_sum > target:
                return

            # Two branches: We continue to use this number, or we move on without using it
            # Continuing to use this number/position
            curr_path.append(candidates[curr_pos])
            generate_combinations(curr_pos, curr_sum + candidates[curr_pos], curr_path)

            # We are not using this number/position. Move on
            curr_path.pop()
            generate_combinations(curr_pos + 1, curr_sum, curr_path)
            return


        generate_combinations(0, 0, [])
        return solution


if __name__ == '__main__':
    test_case = [2, 3, 6, 7]
    target = 7
    solution_instance = Solution()
    print(solution_instance.combinationSum(test_case, target))

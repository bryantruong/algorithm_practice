class Solution:
    def permute(self, nums):
        solution = []

        def dfs(curr_index, visited_set, curr_path):
            # No need to proceed/backtrack since we made copies of the visited_set and curr_path, just return
            if curr_index in visited_set:
                return
            visited_set.add(curr_index)
            curr_path.append(nums[curr_index])
            if len(curr_path) == len(nums):
                # We have formed a new permutation!
                solution.append(curr_path)
                return
            for _ in range(len(nums)):
                # TODO
                # We have to make a copy, since otherwise we would be modifying visited_set and
                # curr_path from lower recursion levels, which we don't want.
                proposed_path = curr_path.copy()
                proposed_visited = visited_set.copy()
                dfs(i, proposed_visited, proposed_path)
            return

        # Create permutations starting from each possible index
        for i in range(len(nums)):
            dfs(i, set(), [])

        return solution


if __name__ == '__main__':
    test_case = [1,2,3]
    solution_instance = Solution()
    print(solution_instance.permute(test_case))

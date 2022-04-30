class Solution:
    def subsets(self, nums):
        solution = [()]  # I am hardcoding the empty list, since this will always be included

        def generate_subsets(current_list):
            # The empty list case is already handled outside of this recursive f(n)
            if len(current_list) == 0:
                return
            # This algorithm will remove an element from each of the possibe indices
            for index_to_remove in range(len(current_list)):
                # Hard copying, since we want to restore the index we remove for later iters
                hard_copied_list = current_list.copy()
                hard_copied_list.pop(index_to_remove)
                generate_subsets(hard_copied_list)
            solution.append(tuple(current_list))
            return

        generate_subsets(nums)
        return set(solution)


if __name__ == '__main__':
    test_case = [1, 2, 3, 4]
    solution_instance = Solution()
    print(solution_instance.subsets(test_case))

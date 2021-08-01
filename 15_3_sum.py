from itertools import permutations


class Solution:
    def threeSum(self, nums):
        solution = []
        solution_set = set()
        # First sort. This will prevent unnecessary calls to two_sum and duplicates
        nums.sort()

        def two_sum(current_list, inverse_target):
            target = -inverse_target
            mappings = {}
            for j, second_triplet in enumerate(current_list):
                desired = target - second_triplet
                if desired in mappings:
                    if (inverse_target, second_triplet, current_list[mappings[desired]]) not in solution_set:
                        solution_set.add((inverse_target, second_triplet, current_list[mappings[desired]]))
                        solution.append([inverse_target, second_triplet, current_list[mappings[desired]]])
                else:
                    # By only adding to the map in the else, we prevent duplicate triplets
                    mappings[second_triplet] = j

        for index, first_triplet in enumerate(nums):
            if first_triplet > 0:
                # It is positive, so there won't be two items after it that sums to zero (since we sorted already)
                return solution
            if index >= 1:
                # Have to check if it is a duplicate
                if nums[index - 1] == first_triplet:
                    continue
                else:
                    two_sum(nums[index + 1:], first_triplet)
            else:
                two_sum(nums[index + 1:], first_triplet)
        return solution


if __name__ == '__main__':
    nums = [0,0,0,0]
    solution_instance = Solution()
    print(solution_instance.threeSum(nums))
    # test_array = [0, 1]
    # index = 0
    # print(test_array[3:3])

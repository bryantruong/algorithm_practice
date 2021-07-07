class Solution:
    """
    Begin greedy/BFS solution. O(N) time complexity
    nums = [2,3,1,1,4]
    """
    def jump(self, nums) -> int:
        left = right = furthest = 0
        levels = 0
        while right < len(nums) - 1:
            for i in range(left, right + 1):
                furthest = max(furthest, nums[i] + i)
            left = right + 1
            right = furthest
            levels += 1
        return levels


    """
    Below was my DP solution. Which is O(n^2) time complexity
    and is O(n) space complexity. The greedy solution (see above)
    is O(N) time complexity and O(1) space complexity.
    """
    # def jump(self, nums) -> int:
    #     cache = [float('inf')] * len(nums)
    #     cache[0] = 0
    #     # We can start from the second index
    #     for index, jump_length in enumerate(nums[:-1]):
    #         if jump_length > 0:
    #             # Update the possible values in the dp array (cache)
    #             for i in range(1, jump_length + 1):
    #                 new_index = index + i
    #                 if new_index >= len(cache):
    #                     break
    #                 if cache[index] + 1 < cache[new_index]:
    #                     cache[new_index] = cache[index] + 1
    #     return cache[-1]


if __name__ == '__main__':
    test_case = [2,3,1,1,4]
    solution_instance = Solution()
    print(solution_instance.jump(test_case))

class Solution:
    def lengthOfLIS(self, nums) -> int:
        # Store the subsequence length up until this point
        cache = [0] * len(nums)
        # We always know that it will be one for the first element
        cache[0] = 1
        for i in range(1, len(nums)):
            biggest_subsequence = 1
            # Check each of the previous values in the array
            for j in range(i):
                # Check if the current value is greater than the previous element
                if nums[j] < nums[i]:
                    potential_best = cache[j] + 1
                    if potential_best > biggest_subsequence:
                        biggest_subsequence = potential_best
            cache[i] = biggest_subsequence
        return max(cache)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_case = [10, 9, 2, 5, 3, 7, 101, 18]
    solution_instance = Solution()
    print(solution_instance.lengthOfLIS(test_case))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Solution:
    def rob(self, nums) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [nums[0], nums[1], nums[0] + nums[2]]
        for i in range(3, len(nums)):
            best_sum = max(dp[i-2] + nums[i], dp[i-3] + nums[i])
            dp.append(best_sum)
        return max(dp[-1], dp[-2])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [12, 2, 1, 18, 14, 3]
    solution_instance = Solution()
    print(solution_instance.rob(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

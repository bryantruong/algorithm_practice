class Solution:
    def twoSum(self, nums, target):
        indices = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indices:
                return (i, indices[diff])
            indices[nums[i]] = i

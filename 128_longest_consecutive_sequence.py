class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_list = set(nums) # O(N)
        max_sequence = 0
        for num in nums:
            if num - 1 in set_list:
                continue # there's no need to to start the traversal if we know we will later
            else:
                curr_sequence = 1
                next_num = num + 1
                while next_num in set_list:
                    curr_sequence += 1
                    next_num += 1
                # Update max_sequence
                max_sequence = max(curr_sequence, max_sequence)
        return max_sequence
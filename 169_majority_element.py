class Solution:
    def majorityElement(self, nums) -> int:
        """
        USING BOYER-MOORE VOTING ALGORITHM (YES, I LOOKED AT THE SOLUTION)
        """
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n

            count += (1 if n == res else -1)
        return res
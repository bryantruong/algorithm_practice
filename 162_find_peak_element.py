class Solution:
    """
    Return the index of the element that is greater than its neighbors
    If multiple peaks, return any of the peaks.
    Imagine that the element before the first element and the element after the last element are -infinity.

    So index 0 or index n-1 can be considered peaks.

    Must run it log n time– Binary search? Linear time solution is extremely easy.
    Input: nums = [1,2,1,3,5,6,4]
    Output: 5

    Input: nums = [1, 2, 3, 4]
    Log n time means we can't even sort it first...
    We could pick the midpoint, then check the neighbors to see if it is greater than those. if so, it return that index.

    If not, do binary search again on the side that is greater than it. Include the current index in the next search.
    From findPeakElement return binary_search()
    binary_search will take in start, stop index. Will return the solution index
        Base case: if greater than both neighbors (including indices -1 and n), return index.
        If not, call binary_search on the half that is bigger than current index.
            - There are cases where both neighbors will be greater than current index. just pick one.
    Prepending -inf and appending -inf would be the easiest, but that would cause an O(N) time
    Do binary search between index 1 to 3
        midpoint = 2
        Do binary search between 2 to 3
    """

    def findPeakElement(self, nums: List[int]) -> int:
        def binary_search(start_i, stop_i):
            midpoint = (start_i + stop_i) // 2
            if midpoint == 0:
                if nums[midpoint + 1] < nums[midpoint]:
                    return midpoint
            elif midpoint == len(nums) - 1:
                if nums[midpoint - 1] < nums[midpoint]:
                    return midpoint
            # We can now assume that len(midpoint) >= 3
            if nums[midpoint - 1] < nums[midpoint] and nums[midpoint + 1] < nums[midpoint]:
                return midpoint
            # If the right neighbor is greater, look at that side
            if nums[midpoint + 1] > nums[midpoint]:
                return binary_search(midpoint, stop_i)
            # Otherwise, look at the left side.
            else:
                return binary_search(start_i, midpoint)

        # Edge case
        if len(nums) == 1:
            return 0
        return binary_search(-1, len(nums))
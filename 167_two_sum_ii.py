class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        This solution uses binary search (log n) for each of the n elements to find n's complement
        """

        def bin_search(start, stop, target):
            while start <= stop:
                # I believe that we will always be in range, but I am leaving it just to be safe.
                midpoint = (start + stop) // 2
                if numbers[midpoint] == target:
                    return midpoint
                if numbers[midpoint] < target:
                    # Search the right half
                    start = midpoint + 1
                else:
                    # Search the left half
                    stop = midpoint - 1
            return -1

        for i in range(len(numbers)):
            num = numbers[i]
            diff = target - num
            # For both scenarios, we search outside of the current index! We can't use any element more than once
            if diff < num:
                # Search the left side of the array for the difference
                found = bin_search(0, i - 1, diff)
            else:
                # Search the right side of the array for the difference
                found = bin_search(i + 1, len(numbers) - 1, diff)

            # The complement was found
            if found > -1:
                return (i + 1, found + 1)
        return
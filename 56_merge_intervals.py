import bisect


class Solution:
    # Below is the solution from Leet Code. my solution was way too convoluted (commented out)
    def merge(self, intervals):
        # First, sort the intervals by their first values
        intervals.sort()
        to_return = []
        i = 0
        to_return.append(intervals[0])
        for interval in intervals:
            # Check for overlap against the last element in the to_return list
            # If previous element (in the to_return list) end is greater than current start, overlap!
            if to_return[-1][1] >= interval[0]:
                # Overlap! Extend the interval only if current interval makes it longer
                if interval[1] > to_return[-1][1]:
                    # Can't modify tuples, so just add a new one
                    to_return[-1] = to_return[-1][0], interval[1]
            else:
                # No overlap, add it to our list to be returned
                to_return.append(interval)
        return to_return

    # My horrible solution:
    # def merge(self, intervals):
    #     # First, sort the intervals by their first values
    #     intervals.sort()
    #     to_return = []
    #     i = 0
    #     curr_max = float("-inf")
    #     while i < len(intervals):
    #         if intervals[i][1] <= curr_max:
    #             i += 1
    #             continue
    #         curr_max = intervals[i][1]
    #         new_interval = (intervals[i][0], curr_max)
    #         while True:
    #             if intervals[i][1] > curr_max:
    #                 curr_max = intervals[i][1]
    #             # We don't need to check forward on the last one, since it would be out of bounds
    #             if i == len(intervals) - 1:
    #                 break
    #             else:
    #                 # Compare the next start value to current stop value
    #                 if intervals[i + 1][0] <= curr_max:
    #                     i += 1
    #                 else:
    #                     # no need to add to the current interval
    #                     break
    #         # Add the stop value of the current interval, but only if it is bigger than current interval.
    #         new_interval = new_interval[0], curr_max
    #         to_return.append(new_interval)
    #         curr_max = new_interval[1]
    #         i += 1
    #     return to_return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_case = [[0, 0], [1, 2], [5, 5], [2, 4], [3, 3], [5, 6], [5, 6], [4, 6], [0, 0], [1, 2], [0, 2], [4, 5]]
    solution_instance = Solution()
    print(solution_instance.merge(test_case))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import bisect


class Solution:
    def merge(self, intervals):
        # First, sort the intervals by their first values
        intervals.sort()
        to_return = []
        i = 0
        curr_max = float("-inf")
        while i < len(intervals):
            if intervals[i][1] <= curr_max:
                i += 1
                continue
            curr_max = intervals[i][1]
            new_interval = (intervals[i][0], curr_max)
            while True:
                if intervals[i][1] > curr_max:
                    curr_max = intervals[i][1]
                # We don't need to check forward on the last one, since it would be out of bounds
                if i == len(intervals) - 1:
                    break
                else:
                    # Compare the next start value to current stop value
                    if intervals[i + 1][0] <= curr_max:
                        i += 1
                    else:
                        # no need to add to the current interval
                        break
            # Add the stop value of the current interval, but only if it is bigger than current interval.
            new_interval = new_interval[0], curr_max
            to_return.append(new_interval)
            curr_max = new_interval[1]
            i += 1
        return to_return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_case = [[0,0],[1,2],[5,5],[2,4],[3,3],[5,6],[5,6],[4,6],[0,0],[1,2],[0,2],[4,5]]
    solution_instance = Solution()
    print(solution_instance.merge(test_case))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

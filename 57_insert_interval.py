import bisect


class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        index_to_insert = bisect.bisect(intervals, newInterval)
        solution_list = intervals[:index_to_insert]
        if not solution_list:
            solution_list.append(newInterval)
        existing_interval = solution_list[-1]
        for interval in [newInterval, *intervals[index_to_insert:]]:
            # If the current interval needs to be merged
            if interval[0] <= existing_interval[1]:
                # Check if it extends the current interval
                if interval[1] > existing_interval[1]:
                    solution_list[-1] = [existing_interval[0], interval[1]]
                    existing_interval = solution_list[-1]
            else:
                solution_list.append(interval)
                existing_interval = solution_list[-1]
        return solution_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_case = [[1, 5]]
    test_new_interval = [0, 3]
    solution_instance = Solution()
    print(solution_instance.insert(test_case, test_new_interval))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

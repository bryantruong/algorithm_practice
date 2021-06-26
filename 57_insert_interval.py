import bisect

class Solution:
    def insert(self, intervals, newInterval):
        new_intervals = []
        # A more normal approach would be to just iterate through from the start and copy over,
        # but I want to try out the bisect Python library.
        if not intervals:
            new_intervals.append(newInterval)
            return new_intervals
        # This index is to the right of the closest index
        closest_index = bisect.bisect(intervals, newInterval)
        new_intervals = intervals[:closest_index]
        curr_index = closest_index - 1
        if new_intervals[curr_index][1] >= newInterval[0]:

            print("This is where we'd replace the back")
        print("Closest Index: " + str(closest_index))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_case = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    test_new_interval = [11,13]
    solution_instance = Solution()
    print(solution_instance.insert(test_case, test_new_interval))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

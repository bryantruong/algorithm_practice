# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        # Note: use .sort() for lists, since it modifies it in-place. For other iterables, you must use sorted()
        intervals.sort()
        for i in range(1, len(intervals)):
            # Check if the previous stop time is after the next start time
            if intervals[i - 1][1] > intervals[i][0]:
                return False
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    test_case = [[0,30],[5,10],[15,20]]
    solution_instance = Solution()
    print(solution_instance.canAttendMeetings(test_case))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

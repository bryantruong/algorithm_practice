# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import heapq


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        intervals.sort()
        rooms = []  # This an empty list, but will turn into a heapify once we push to it.
        heapq.heappush(rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            # If there is going to be a room available
            if rooms[0] <= intervals[i][0]:
                # Remove that room, since we will need to update the entry with when the room will actually be free.
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i][1])
        return len(rooms)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    test_case = [[0, 30], [5, 10], [15, 20]]
    solution_instance = Solution()
    print(solution_instance.minMeetingRooms(test_case))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

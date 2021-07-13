import bisect


class Solution:
    def insert(self, intervals, newInterval):
        bisect.insort(intervals, newInterval)
        # Now just call the merge routine with this unmerged list
        return self.merge(intervals)

    def merge(self, intervals_list):
        """
        Helper function to merge the list. Is not in place, will return a copy of the original array
        if there were no merges that needed to take place.
        :param intervals_list: the list of intervals that may/may not need to be merged
        :return: the merged list
        """
        solution_list = [intervals_list[0]]
        existing_interval = solution_list[0]
        for interval in intervals_list:
            # If the current interval needs to be merged
            if interval[0] <= existing_interval[1]:
                # Check if it extends the current interval
                if interval[1] > existing_interval[1]:
                    solution_list[-1] = [existing_interval[0], interval[1]]
                    existing_interval = [existing_interval[0], interval[1]]
            else:
                solution_list.append(interval)
                existing_interval = solution_list[-1]
        return solution_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_case = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    test_new_interval = [11, 13]
    solution_instance = Solution()
    print(solution_instance.insert(test_case, test_new_interval))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

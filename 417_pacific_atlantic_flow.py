from collections import deque


class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []
        num_of_rows = len(heights)
        num_of_columns = len(heights[0])

        # We will store the INDICES in here. Will need to consult the heights matrix for actual heights
        pacific_queue = deque()
        atlantic_queue = deque()

        for i in range(num_of_rows):
            pacific_queue.append((i, 0))  # Pacific should start with the first column
            atlantic_queue.append((i, num_of_columns - 1))  # Atlantic should start with the last column

        for i in range(num_of_columns):
            pacific_queue.append((0, i))  # Pacific should start with the first row
            atlantic_queue.append((num_of_rows - 1, i))  # Atlantic should start with the last row

            def bfs(queue):
                visited = set()
                while queue:
                    row, col = queue.popleft()
                    visited.add((row, col))
                    # down one, up one, left one, right one
                    for (row_change, column_change) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        new_row, new_col = row + row_change, col + column_change
                        if new_row < 0 or new_row > (num_of_rows - 1) or new_col < 0 or new_col > (num_of_columns - 1):
                            # Skip this cell if it is out of bounds
                            continue
                        # Now check if the ocean can flow up it. If so, we'll want to visit it later
                        if heights[new_row][new_col] > heights[row][col]:
                            queue.append((new_row, new_col))
                return visited
        pacific_results = bfs(pacific_queue)
        atlantic_results = bfs(atlantic_queue)

        # Get the intersection of the results, returns a set, so cast to list
        return list(pacific_results.intersection(atlantic_results))

if __name__ == '__main__':
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    solution_instance = Solution()
    print(solution_instance.pacificAtlantic(heights))

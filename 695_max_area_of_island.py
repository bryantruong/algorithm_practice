class Solution:
    """
    This is a classic DFS problem.
    Iterate through every cell in the grid.
    Perform a DFS (checking each direction and boundaries) on each island.
    For each DFS, keep track of the number of cells added
    Keep a visited set to prevent time being wasted/infinite recursion

    Time complexity: O(m x n) + number of island cells
    Space complexity: O(m x n) if the whole grid is one entire island
    """

    def maxAreaOfIsland(self, grid) -> int:
        def on_board(row_index, col_index):
            if 0 <= row_index <= len(grid) - 1 and 0 <= col_index <= len(grid[0]) - 1:
                return True
            return False

        def dfs(row, col, curr_area):
            # Directional changes: Up, down, left, right
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + delta_row, col + delta_col
                if on_board(new_row, new_col) and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    if grid[new_row][new_col] == 1:
                        curr_area += 1
                        curr_area = dfs(new_row, new_col, curr_area)
            return curr_area

        visited = set()
        max_area = 0
        for row_i in range(len(grid)):
            for col_i in range(len(grid[0])):
                visited.add((row_i, col_i))
                if grid[row_i][col_i] == 1 and grid[row_i][col_i] not in visited:
                    max_area = max(dfs(row_i, col_i, 1), max_area)
        return max_area


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    test_grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                 [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    solution_instance = Solution()
    solution_to_return = solution_instance.maxAreaOfIsland(test_grid)
    print(solution_to_return)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from collections import deque


class Solution:
    def numIslands(self, grid) -> int:
        visited = set()
        island_count = 0

        def traverse_island(row_index, column_index):
            # We should only be here if it hasn't been visited
            visited.add((row_index, column_index))
            # Up, down, left, right
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row_index + delta_row, column_index + delta_col
                # Check that it is in bounds
                if 0 <= new_row <= len(grid) - 1 and 0 <= new_col <= len(grid[0]) - 1 and (new_row, new_col) \
                        not in visited:
                    # Check if it's a land cell
                    if grid[new_row][new_col] == '1':
                        # Recurse via dfs
                        traverse_island(new_row, new_col)
            # After checking all the neighbors return
            return

        for row_i, row in enumerate(grid):
            for col_i, cell_val in enumerate(row):
                # We only want to dfs on land cells that haven't been visited yet
                if cell_val == '1' and (row_i, col_i) not in visited:
                    # Call the DFS function
                    traverse_island(row_i, col_i)
                    island_count += 1

        return island_count
if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    solution_instance = Solution()
    # This problem doesn't ask us to return anything, so won't print
    print(solution_instance.numIslands(grid))

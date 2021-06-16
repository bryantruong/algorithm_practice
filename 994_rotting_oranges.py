from collections import deque


class Solution:
    def orangesRotting(self, grid) -> int:
        """
        :param grid: The grid
        :return: Number of iterations until no cell has a fresh orange
        """

        def check_need_to_change(row, col, grid):
            # Check if out of bounds
            if row > len(grid) - 1 or row < 0 or col > len(grid[0]) - 1 or col < 0:
                return False
            if grid[row][new_col] == 0 or grid[row][new_col] >= 2:
                return False
            return True

        if not grid or not grid[0]:
            # There are no cells, so no iterations needed to remove fresh oranges.
            return 0
        # Use a queue for BFS
        grid_queue = deque()
        # Use a set to store the cells with fresh oranges
        fresh_cells = set()
        for row_i in range(len(grid)):
            for col_i in range(len(grid[0])):
                curr_val = grid[row_i][col_i]
                if curr_val == 2:
                    grid_queue.append((row_i, col_i))
                elif curr_val == 1:
                    fresh_cells.add((row_i, col_i))
        # Edge case, where no fresh oranges exist
        if not fresh_cells:
            return 0
        # Create a set to store the changed cells
        new_rotten_set = set()
        # Start BFS from the rotten oranges
        max_val = 2
        while grid_queue:
            curr_row, curr_col = grid_queue.popleft()
            # Try out all of the 4-adjacent operations: up, down, left, right
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = curr_row + delta_row, curr_col + delta_col
                if check_need_to_change(new_row, new_col, grid):
                    new_val = grid[curr_row][curr_col] + 1
                    if new_val > max_val:
                        max_val = new_val
                    grid[new_row][new_col] = new_val
                    new_rotten_set.add((new_row, new_col))
                    grid_queue.append((new_row, new_col))
        still_fresh = fresh_cells.difference(new_rotten_set)
        if still_fresh:
            return -1
        else:
            return max_val - 2


if __name__ == '__main__':
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    solution_instance = Solution()
    # This problem doesn't ask us to return anything, so won't print
    print(solution_instance.orangesRotting(grid))

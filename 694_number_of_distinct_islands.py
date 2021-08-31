class Solution:
    """
    We need tto store the characteristics of each island.
    if we store number of rows and columns in each island is that enough?

    Could we store the directions in which we explored each island? May work if we start dfs from the same relative
    position for each island.

    General Approach:
    Iterate through each cell in the array, going left to right, top down (row major?)
    Keep track of the cells that have been visited. Only perform DFS if they haven't been visited.

    If the cell is a 1 and is not yet visited, perform a dfs subroutine. Initialize a list which will store the actions
    taken when exploring the island.

    Check the neighbors in this order:
        Up, down, left, right. If neighbor is in bounds, mark it is as visited. If it has a value of 1,
        call dfs subroutine with this node. Add this action to the list.
        After exploring each of the neighbors, return.
    Convert the list of actions taken to a tuple, and add that to our islands set.

    Return the size of the islands set.

    Go through each element O(M x N). The DFS would add in the wort case O(M x N), which is if the entire
    grid was one island. Converting the list to a tuple could be O(M x N). Overall, still O(M x N).

    Space complexity: Store the directions explored for each island, which could be O(M x N). O(M x N)
    to store the visited nodes. Overall, still O(M x N).
    """

    def numDistinctIslands(self, grid) -> int:

        def explore_island(row_index, col_index, depth):
            # Mark this cell as visited
            grid[row_index][col_index] = 0
            # Explore each of the neighbors. Up, Down, Left, Right
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor_row = row_index + delta_row
                neighbor_col = col_index + delta_col
                # First check if in bounds
                if 0 <= neighbor_row <= len(grid) - 1 and 0 <= neighbor_col <= len(grid[0]) - 1:
                    # Check if the neighboring cell's value is a 1
                    if grid[neighbor_row][neighbor_col] == 1:
                        # Record the action we are taking
                        actions.append((delta_row, delta_col, depth + 1))
                        explore_island(neighbor_row, neighbor_col, depth + 1)
            return

        # Store the island direction tuples in here
        islands = set()
        # Iterate through each cell in the grid.
        for row_i in range(len(grid)):
            for col_i in range(len(grid[0])):
                if grid[row_i][col_i] == 1:
                    actions = []
                    explore_island(row_i, col_i, 0)
                    islands.add(tuple(actions))
        return len(islands)


if __name__ == '__main__':
    grid = [[1, 1, 0],  # First island: [((0, 1), 1), ((1, 0), 2), ((0, 1), 3)]
            [0, 1, 1],  # 2     island: [((0, 1), 1), ((1, 0), 2), ((0, 1), 2)]
            [0, 0, 0],
            [1, 1, 1],
            [0, 1, 0]]
    solution_instance = Solution()
    print(solution_instance.numDistinctIslands(grid))

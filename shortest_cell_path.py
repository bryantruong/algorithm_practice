from collections import deque


def is_valid(row, col, matrix):
    if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix[0]) - 1 and \
            matrix[row][col] == 1:
        return True
    return False


def shortestCellPath(grid, sr, sc, tr, tc):
    # This is a BFS approach
    curr_length = -1
    visited = set()
    to_visit = deque()
    to_visit.append((sr, sc))
    while to_visit:
        no_of_iters = len(to_visit)
        curr_length += 1
        for _ in range(no_of_iters):
            curr_row, curr_col = to_visit.popleft()
            visited.add((curr_row, curr_col))
            if (curr_row, curr_col) == (tr, tc):
                return curr_length
            # Check each direction/change: Up, right, down, left, respectively
            for delta_row, delta_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row, new_col = curr_row + delta_row, curr_col + delta_col
                if is_valid(new_row, new_col, grid) and (new_row, new_col) not in visited:
                    to_visit.append((new_row, new_col))
    return -1


if __name__ == '__main__':
    test_grid = [[1, 1, 1, 1],
                 [1, 0, 0, 1],
                 [1, 1, 1, 1]]
    print(shortestCellPath(test_grid, 0, 0, 2, 0))

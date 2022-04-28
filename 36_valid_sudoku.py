class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        This is my brute force solution. Not far off from the actual solution actually!

        """
        # check the rows
        for row_i in range(9):
            row_set = set()
            for col_i in range(9):
                if board[row_i][col_i] == '.':
                    continue
                if board[row_i][col_i] in row_set:
                    return False
                else:
                    row_set.add(board[row_i][col_i])
        # check the cols
        for col_i in range(9):
            col_set = set()
            for row_i in range(9):
                if board[row_i][col_i] == ".":
                    continue
                if board[row_i][col_i] in col_set:
                    return False
                else:
                    col_set.add(board[row_i][col_i])
                    # check each 3x3 grid, row by row
        for row_offset in [0, 3, 6]:
            for col_offset in [0, 3, 6]:
                grid_set = set()
                for grid_row in range(3):
                    for grid_col in range(3):
                        if board[grid_row + row_offset][grid_col + col_offset] == '.':
                            continue
                        if board[grid_row + row_offset][grid_col + col_offset] in grid_set:
                            return False
                        else:
                            grid_set.add(board[grid_row + row_offset][grid_col + col_offset])
        return True
class Solution:
    def exist(self, board, word) -> bool:
        def word_search(curr_row, curr_col, index, curr_path):
            if curr_row < 0 or curr_row > len(board) - 1 or curr_col < 0 or curr_col > len(board[0]) - 1:
                # We also need to backtrack and remove
                return False
            if board[curr_row][curr_col] == word[index]:
                if index == len(word) - 1:
                    return True
                found = False
                # This letter matches
                curr_path.add((curr_row, curr_col))
                for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_row = curr_row + delta_row
                    new_col = curr_col + delta_col
                    if (new_row, new_col) not in curr_path:
                        found = word_search(new_row, new_col, index + 1, curr_path)
                        if found:
                            return True
                curr_path.remove((curr_row, curr_col))
            return False

        for row_i in range(len(board)):
            for col_i in range(len(board[0])):
                found = False
                if board[row_i][col_i] == word[0]:
                    found = word_search(row_i, col_i, 0, set())
                    if found:
                        return True
        return False


if __name__ == '__main__':
    test_case = [["a","a","a"],["A","A","A"],["a","a","a"]]
    test_word = word = "aAaaaAaaA"
    solution_instance = Solution()
    print(solution_instance.exist(test_case, test_word))

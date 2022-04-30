class Solution:
    def exist(self, board, word) -> bool:
        def search(visited, curr_coords, word_index):
            """
            :param visited: Set of visited cells. Once we visit a cell, it cannot be used again.
            :param curr_coords: (curr_row_i, curr_col_i)
            :param word_index: the index of the letter in the word we are looking to match
            :return: boolean
            """
            # Mark the current cell as visited.
            visited.add(curr_coords)
            # Base Case for a successful search
            if word_index == len(word):
                return True
            curr_row, curr_col = curr_coords
            # Up, down, left, right
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row = curr_row + delta_row
                new_col = curr_col + delta_col
                if 0 <= new_row <= len(board) - 1 and 0 <= new_col <= len(board[0]) - 1 and (new_row, new_col) \
                        not in visited:
                    new_val = board[new_row][new_col]
                    if new_val == word[word_index]:
                        # Continue the search from this next cell
                        successful = search(visited, (new_row, new_col), word_index + 1)
                        if successful:
                            return True
                        # Backtrack and remove the cell from the visited set
                        else:
                            # Backtrack
                            visited.remove((new_row, new_col))
            # If we iterated through the neighbors and completed the searches for possible paths but no luck:
            return False

        for row_i in range(len(board)):
            for col_i in range(len(board[0])):
                if board[row_i][col_i] == word[0]:
                    search_successful = search(set(), (row_i, col_i), 1)
                    if search_successful:
                        return True
        return False


if __name__ == '__main__':
    test_case = [["a","a","a"],["A","A","A"],["a","a","a"]]
    test_word = word = "aAaaaAaaA"
    solution_instance = Solution()
    print(solution_instance.exist(test_case, test_word))

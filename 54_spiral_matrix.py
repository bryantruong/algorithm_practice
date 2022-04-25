class Solution:
    def spiralOrder(self, matrix):
        # Establish the pointer indices
        start_row = 0
        start_col = 0
        end_row = len(matrix) - 1
        end_col = len(matrix[0]) - 1

        directions = ['RIGHT', 'DOWN', 'LEFT', 'UP']
        counter = 0
        output = []

        while start_row <= end_row and start_col <= end_col:
            curr_direction = directions[counter % 4]  # Since there are four directions
            if curr_direction == 'RIGHT':
                for col_i in range(start_col, end_col + 1):  # Add one because the stop index is not inclusive
                    output.append(matrix[start_row][col_i])
                start_row += 1
            elif curr_direction == 'DOWN':
                for row_i in range(start_row, end_row + 1):
                    output.append(matrix[row_i][end_col])
                end_col -= 1
            elif curr_direction == 'LEFT':
                for col_i in range(end_col, start_col - 1, -1):
                    output.append(matrix[end_row][col_i])
                end_row -= 1
            elif curr_direction == 'UP':
                for row_i in range(end_row, start_row - 1, -1):
                    output.append(matrix[row_i][start_col])
                start_col += 1
            counter += 1
        return output
def spiral_copy(inputMatrix):
    start_row = 0
    stop_row = len(inputMatrix)
    start_col = 0
    stop_col = len(inputMatrix[0])
    output = []
    while start_row <= stop_row - 1 and start_col <= stop_col - 1:
        for col_index in range(start_col, stop_col):
            output.append(inputMatrix[start_col][col_index])
        start_row += 1
        for row_index in range(start_row, stop_row):
            output.append(inputMatrix[row_index][stop_col - 1])
        stop_col -= 1
        if start_row <= stop_row - 1:
            for col_index in range(stop_col - 1, start_col - 1, -1):
                output.append(inputMatrix[stop_row - 1][col_index])
            stop_row -= 1
        if start_col <= stop_col - 1:
            for row_index in range(stop_row - 1, start_row - 1, -1):
                output.append(inputMatrix[row_index][start_col])
            start_col += 1
    return output


if __name__ == '__main__':
    # print(spiral_copy([[1, 2]]))

    new_array = [[None for row in range(3)] for col in range(5)]
    print("array made")
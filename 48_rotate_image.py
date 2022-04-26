class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix) - 1
        top = 0
        bottom = len(matrix[0]) - 1  # Technically, we can use left and right here, since it's a square

        while left <= right and top <= bottom:
            for offset in range(right - left):
                # Save the top left element into a temp. this will eventually go into the top right
                temp = matrix[top][left + offset]

                matrix[top][left + offset] = matrix[bottom - offset][left]
                # We can overwrite the bottom left, since it's already been moved
                matrix[bottom - offset][left] = matrix[bottom][right - offset]

                # We can overwrite the bottom right, since it's already been moved
                matrix[bottom][right - offset] = matrix[top + offset][right]

                # Place the original top left into the top right
                matrix[top + offset][right] = temp
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return
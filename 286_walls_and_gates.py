from collections import deque
class Solution:
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return []
        rooms_queue = deque()
        # Iterate through each cell
        for row_i in range(len(rooms)):
            for col_i in range(len(rooms[0])):
                # Check if the cell is a "gate"
                if rooms[row_i][col_i] == 0:
                    # Start BFS from the gates
                    rooms_queue.append((row_i, col_i))
        while rooms_queue:
            curr_row, curr_col = rooms_queue.popleft()
            for row_change, col_change in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Moving up, down, left, right
                new_row, new_col = curr_row + row_change, curr_col + col_change
                if 0 <= new_row <= len(rooms) - 1 and 0 <= new_col <= len(rooms[0]) - 1 and rooms[new_row][new_col] > rooms[curr_row][curr_col]:
                            rooms[new_row][new_col] = rooms[curr_row][curr_col] + 1
                            rooms_queue.append((new_row, new_col))
        print(rooms)
if __name__ == '__main__':
    rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    solution_instance = Solution()
    # This problem doesn't ask us to return anything, so won't print
    solution_instance.wallsAndGates(rooms)

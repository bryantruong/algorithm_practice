# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = (0, 0)
        i = 0
        directions = ['N', 'E', 'S', 'W']
        card_to_coord = {'N': (0, 1),
                         'E': (1, 0),
                         'S': (0, -1),
                         'W': (-1, 0)
                         }
        for instruction in instructions:
            if instruction == 'G':
                coord_change = directions[i % 4]
                new_x = position[0] + card_to_coord[coord_change][0]
                new_y = position[1] + card_to_coord[coord_change][1]
                position = new_x, new_y
            elif instruction == 'L':
                i -= 1
            elif instruction == 'R':
                i += 1
        if position == (0,0) or i % 4 != 0:
            return True
        return False
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    instructions = "GL"
    solution_instance = Solution()
    print(solution_instance.isRobotBounded(instructions))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

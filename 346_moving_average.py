# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Variables from brute force
        """
        # self.numbers_list = []
        # self.size = size
        """
        Variables for better solution
        """
        self.window = deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.window) < self.size:
            # Update sum
            self.sum += val
            # Put in the most recent value
            self.window.append(val)
        else:
            # len(self.window) should never be bigger than self.size
            front_element = self.window.popleft()
            # Subtract the old element from the sum
            self.sum -= front_element
            # Add the new element to the sum
            self.sum += val
            # Put in the new value to the window
            self.window.append(val)
        return self.sum / len(self.window)


"""
This was a brute force solution. A better solution is uncommented.
"""
    # def next(self, val: int) -> float:
    #     self.numbers_list.append(val)
    #     sum = 0
    #     num_of_values = 0
    #     for i in range(-1, -self.size - 1, -1):
    #         if -i > len(self.numbers_list):
    #             break
    #         else:
    #             sum += self.numbers_list[i]
    #             num_of_values += 1
    #     return sum / num_of_values



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = MovingAverage(3)
    print(obj.next(1))
    print(obj.next(10))
    print(obj.next(3))
    print(obj.next(5))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        I believe the key is recognizing that we move the one that is smaller inwards.
        Why? Because the one that is smaller dictates the height that we can use for the area calculation
        By moving the smaller one inwards, we are hoping that we can find a taller height, while keeping the
        other constant, as it is already a somewhat-decent height.
        """
        back = len(height) - 1
        front = 0
        max_area = 0
        # We are guaranteed to have at least two elements in the height array
        while front < back:
            curr_area = min(height[front], height[back]) * (back - front)
            if curr_area > max_area:
                max_area = curr_area
            # Move inwards
            if height[front] < height[back]:
                front += 1
            else:
                back -= 1
        return max_area


if __name__ == '__main__':
    solutionObject = Solution()
    test_height = [3, 9, 3, 4, 7, 2, 12, 6]
    print(solutionObject.maxArea(test_height))

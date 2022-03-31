class NumArray:

    def __init__(self, nums):
        self.nums = [0]
        for number in nums:
            self.nums.append(self.nums[-1] + number)

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right + 1] - self.nums[left]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num_array_obj = NumArray([-2, 0, 3, -5, 2, -1])
    """
    [0, -2, -2, 1, -4, -2, -3]
    
    Why do we need a zero index?
    [-2, -2, 1, -4, -2, -3]
    
    sumRange(1,3) should return -2
    
    -4 represents the sum from 0 to 3 inclusive. We don't want the first one, so subtract the -2
    """

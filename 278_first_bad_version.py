# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        start = 1
        stop = n
        while start < stop:
            midpoint = (start + stop) // 2
            if isBadVersion(midpoint):
                stop = midpoint
            else:
                # Midpoint was good, but the right neighbor is bad. Right neighbor is the solution
                start = midpoint + 1
        return start


"""
We are given n versions, in a list. Want to find the first bad one
Check if a version is bad by calling isBadVersion(version), which is already implemented for us.

The naive solution would just be to start from n = 1 and call isBadVersion each time

[Y, Y, Y, Y, N, N, N]

Edge case: if n = 1, return 1
Is there a binary search solution?
You could pick the mid point and check the validity of midpoint and of its neighbors.
    If midpoint and neighbors are both Y, choose right half
    If midpoint is Y and one of the neighbors is N, then return the neighbor's index
    If midpoint is N and one of the neighbors is Y, then return the midpoint's index
    If midpoint is N and both neighbors are N, choose left half
    
    Repeat. Should never run infinitely, since it is given that there was a defect.
    
"""

if __name__ == '__main__':
    # test_nums = "88"
    # solution_instance = Solution()
    # print(solution_instance.isStrobogrammatic(test_nums))
    string = "1"
    print(string[0:])

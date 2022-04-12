from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root):
        averages = []
        last_in_level = root
        to_visit = deque()
        to_visit.append(root)
        curr_sum = 0
        level_count = 0
        while to_visit: 
            curr_node = to_visit.popleft()
            if curr_node.left:
                to_visit.append(curr_node.left)
            if curr_node.right:
                to_visit.append(curr_node.right)
            curr_sum += curr_node.val
            level_count += 1
            if curr_node == last_in_level:
                averages.append(curr_sum/level_count)
                curr_sum = 0
                level_count = 0
                if to_visit:
                    last_in_level = to_visit[-1]
        return averages
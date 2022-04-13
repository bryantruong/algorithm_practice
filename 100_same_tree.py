# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:  # Base Case
            return True
        if not p or not q:  # One of the two is Null, while the other is non-null
            return False
        if p.val != q.val:  # We are computing this for the roots, for others we can assume they match
            return False
        left_matches = self.isSameTree(p.left, q.left)  # check left subtree
        right_matches = self.isSameTree(p.right, q.right)  # check right subtree
        return left_matches and right_matches


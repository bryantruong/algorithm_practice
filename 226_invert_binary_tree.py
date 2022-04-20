# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        # Base case, we are past a leaf
        if not root:
            return None
        # Temp variable to store the original left subtree before we rewrite
        old_left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(old_left)
        return root

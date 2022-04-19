# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        # First, do a BFS to see find the matching root.
        nodes = deque()
        nodes.append(root)

        def check_subtree(parent, sub):
            """
            Helper DFS function to check for subtrees
            """
            if parent.val != sub.val:
                return False
            left_matches = False
            right_matches = False
            # If both right children are non-null, we need to check their subtrees
            if parent.right and sub.right:
                right_matches = check_subtree(parent.right, sub.right)
            # If both right children are null, then they match
            if not parent.right and not sub.right:
                right_matches = True
            # If both left children are non-null, we need to check their subtrees
            if parent.left and sub.left:
                left_matches = check_subtree(parent.left, sub.left)
            # If both left children are null, then they match
            if not parent.left and not sub.left:
                left_matches = True
            return left_matches and right_matches

        while nodes:
            curr = nodes.popleft()
            if curr.val == subRoot.val:
                if check_subtree(curr, subRoot) == True:
                    return True
            if curr.left:
                nodes.append(curr.left)
            if curr.right:
                nodes.append(curr.right)
        return False

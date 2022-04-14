# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
DISCLAIMER: This is not a good solution. There's actually no need for a parent calling function.
"""
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False

        def calculate_sums(curr_node, curr_sum):
            curr_sum += curr_node.val  # We can assume that the current node is not null
            if not curr_node.left and not curr_node.right:  # When we reach a leaf, check if the sum matches
                if curr_sum == targetSum:
                    return True
                return False
            left_matches = False
            right_matches = False
            # If it isn't a leaf, continue to tabulate the sum as we recurse down the tree, both L and R (if non-null)
            if curr_node.left:
                left_matches = calculate_sums(curr_node.left, curr_sum)
            if curr_node.right:
                right_matches = calculate_sums(curr_node.right, curr_sum)
            return left_matches or right_matches

        return calculate_sums(root, 0)


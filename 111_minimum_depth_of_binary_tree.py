# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root) -> int:
        """
        :param root: Optional
        :return: the number of nodes along the shortest path from the root node down to the nearest leaf node.

        This is the DFS solution, which is less efficient than the BFS solution.
        """

        def get_min_depth(curr_node, path_length):
            # If the current node is a leaf, we can stop
            if not curr_node.left and not curr_node.right:
                return path_length
            # If there is only a right child, explore that right child ONLY
            if not curr_node.left:
                return get_min_depth(curr_node.right, path_length + 1)
            if not curr_node.right:
                # If there is only a left child, explore that left child ONLY
                return get_min_depth(curr_node.left, path_length + 1)
            # The current node has two children, so we have to explore both.
            return min(get_min_depth(curr_node.left, path_length + 1),
                       get_min_depth(curr_node.right, path_length + 1))

        if not root:
            return 0
        else:
            # Kick off the recursive function
            return get_min_depth(root, 1)

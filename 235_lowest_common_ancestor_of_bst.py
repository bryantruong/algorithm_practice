# This is a sample Python script.
from collections import deque


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Helper recursive function that creates the binary tree from a list
def createBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] is None:
            return
        pNode = TreeNode(data[index])
        pNode.left = createBTree(data, 2 * index + 1)  # [1, 3, 7, 15, ...]
        pNode.right = createBTree(data, 2 * index + 2)  # [2, 5, 12, 25, ...]
    return pNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        The secret is to realize that at each node, we have three options:
        1. p and q are both less than current node, look in left subtree.
        2. p and q are both greater than current node, so look in the right subtree.
        3. p or q equals the current node, or only one of the two is greater. This means we found it!
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    tree = createBTree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 0)
    solution_instance = Solution()
    solution_to_return = solution_instance.lowestCommonAncestor(tree, TreeNode(val=2), TreeNode(val=4))
    print(solution_to_return.val)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

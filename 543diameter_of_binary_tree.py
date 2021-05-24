# This is a sample Python script.

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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0
        def getLongestPath(current_root) -> int:
            nonlocal diameter
            if not current_root:
                return 0
            longest_right = getLongestPath(current_root.right)
            longest_left = getLongestPath(current_root.left)
            diameter_through_current_root = longest_left + longest_right
            diameter = max(diameter, diameter_through_current_root)
            # The longest path from that node to a leaf is the max of longest_left and longest_right + 1
            return max(longest_left, longest_right) + 1
        getLongestPath(root)
        return diameter

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create the tree
    tree = createBTree([1,2,3,4,5, None, None,None, None, 6, None,7, None,], 0)
    solution_instance = Solution()
    solution_to_return = solution_instance.diameterOfBinaryTree(tree)
    print(solution_to_return)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

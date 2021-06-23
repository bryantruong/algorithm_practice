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
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check_validity(float('inf'), float('-inf'), root)

    def check_validity(self, max_val, min_val, curr_node):
        # Base Case
        if not curr_node:
            return True
        if curr_node.val >= max_val or curr_node.val <= min_val:
            return False
        # Check left subtree
        left_valid = self.check_validity(curr_node.val, min_val, curr_node.left)
        if left_valid:
            # Check the right subtree
            right_valid = self.check_validity(max_val, curr_node.val, curr_node.right)
            if right_valid:
                return True
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    s = createBTree([5, 1, 4, None, None, 3, 6], 0)
    solution_instance = Solution()
    solution_to_return = solution_instance.isValidBST(s)
    print(solution_to_return)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

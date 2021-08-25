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
    """
    Program Inorder Traversal (Left, Root, Right). Return the traversal as a list.
           1
         /  \
       2     3
      / \
     4   5
    """

    def inorderTraversal(self, root):
        solution_list = []

        def dfs(root_node):
            if not root_node:
                return
            # Expand the left child
            dfs(root_node.left)
            # Print the current root value
            solution_list.append(root_node.val)
            # Expand the right child
            dfs(root_node.right)
            return

        dfs(root)
        return solution_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    s = createBTree([10, 5, 15, 3, 7, None, 18], 0)
    solution_instance = Solution()
    solution_to_return = solution_instance.rangeSumBST(s, 7, 15)
    print(solution_to_return)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

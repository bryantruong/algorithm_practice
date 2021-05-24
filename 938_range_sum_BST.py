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
    # def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
    #     def traverse_add(root, low, high, current_sum):
    #         if not root:
    #             return current_sum
    #         # Add the current node's value to the sum
    #         if low <= root.val <= high:
    #             current_sum += root.val
    #         # Traverse the left subtree if we need to and update current_sum
    #         if root.val > low:
    #             current_sum = traverse_add(root.left, low, high, current_sum)
    #         # Traverse the right subtree if we need to and update current_sum
    #         if root.val < high:
    #             current_sum = traverse_add(root.right, low, high, current_sum)
    #         return current_sum
    #     return traverse_add(root, low, high, 0)
    #

    # Below is the LC solution. Same thing, but cleaner and uses a class level variable. Not good practice to use them.
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    s = createBTree([10, 5, 15, 3, 7, None, 18], 0)
    solution_instance = Solution()
    solution_to_return = solution_instance.rangeSumBST(s, 7, 15)
    print(solution_to_return)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

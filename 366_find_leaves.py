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
    def findLeaves(self, root: TreeNode) -> bool:
        """
        BFS approach won't work; it doesn't keep track of what is a leaf. Just levels
        DFS and make lists when we reach leaves
        Also need to mark the visited ones as None to "remove" them

        Time complexity: We want to only visit each node/edge ONCE
        Not sure how to do that though. Think we will have to start from the root each time
        May get TLE...
        O(V+E) times the max height of the tree
        """
        final_sol = []

        def perform_dfs(curr_node, curr_leaves):
            # This logic doesn't work, because it will delete everything below it.
            curr_length = len(curr_leaves)
            if not curr_node.left and not curr_node.right:
                curr_leaves.append(curr_node.val)
            # Look at the left subtree if it's non-null
            if curr_node.left:
                perform_dfs(curr_node.left, curr_leaves)
                # We need to mark the node's child as None, since we don't want to go down there again
                if len(curr_leaves) > curr_length:
                    curr_node.left = None
            # Look at the right subtree
            if curr_node.right:
                perform_dfs(curr_node.right, curr_leaves)
                # We need to mark the node's child as None, since we don't want to go down there again
                if len(curr_leaves) > curr_length:
                    curr_node.right = None
            return curr_leaves

        final_sol.append(perform_dfs(root, []))
        return final_sol


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    s = createBTree([1, 2, 3, 4, 5], 0)
    solution_instance = Solution()
    solution_to_return = solution_instance.findLeaves(s)
    print(solution_to_return)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

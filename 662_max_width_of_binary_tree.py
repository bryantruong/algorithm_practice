from collections import deque


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
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        max_width = 0
        traversal_queue = deque()
        # This queue should never have null entries
        traversal_queue.append((root, 1))
        while traversal_queue:
            _, left_index = traversal_queue[0]
            _, right_index = traversal_queue[-1]
            max_width = max(max_width, (right_index - left_index) + 1)
            # Complete BFS, adding non-null children to the queue. Only run for this level
            for _ in range(len(traversal_queue)):
                # Pop node off queue
                curr_node, curr_index = traversal_queue.popleft()
                if curr_node.left:
                    traversal_queue.append((curr_node.left, curr_index * 2))
                if curr_node.right:
                    traversal_queue.append((curr_node.right, (curr_index * 2) + 1))

        return max_width


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create the tree
    tree = createBTree([1, 3, 2, 5, None, None, 9, 6, None, None, 7], 0)
    solution_instance = Solution()
    solution_to_return = solution_instance.widthOfBinaryTree(tree)
    print(solution_to_return)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

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
        DAMN this was bad. If you are studying LC with me, don't use this solution lol
        I somehow didn't think of doing just one search, and comparing the current node to the values
        of both p and q at the same time!
        :param root:
        :param p:
        :param q:
        :return:
        """
        visited_to_p = set()
        visited_to_q = deque()

        def find_node(curr_node, is_for_p):
            # We don't need to worry about if curr_node is null, since we are guaranteed to find it in the tree.
            if is_for_p:
                visited_to_p.add(curr_node)
                target = p
            else:
                visited_to_q.append(curr_node)
                target = q
            if curr_node.val == target.val:
                return
            else:
                # Do a Binary search down the tree
                if curr_node.val < target.val:
                    find_node(curr_node.right, is_for_p)
                else:
                    find_node(curr_node.left, is_for_p)
            return

        find_node(root, True)
        find_node(root, False)
        lca = None
        visited_to_q.pop()
        while visited_to_q:
            path_node = visited_to_q.pop()
            if path_node in visited_to_p:
                lca = path_node
                return lca
        return lca


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    tree = createBTree([2, 1], 0)
    solution_instance = Solution()
    solution_to_return = solution_instance.lowestCommonAncestor(tree, TreeNode(val=1), TreeNode(val=2))
    print(solution_to_return.val)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

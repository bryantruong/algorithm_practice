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
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def check_flip_equivs(node1, node2):
            """
            Recursive call to traverse both trees. First checks to ensure the current nodes are equal.
            Calls itself to traverse the minimum child of both graphs before traversing the other.
            Base cases are when the nodes are not equal or both nodes are None
            """
            # Base Cases
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False

            graph_1_left, graph_1_right = node1.left, node1.right
            graph_2_left, graph_2_right = node2.left, node2.right
            # Will have to use a lambda function so that None values are sorted to the front.
            graph_1_order = sorted([node1.left, node1.right], key=lambda x: float('-inf') if x is None else x.val)
            graph_2_order = sorted([node2.left, node2.right], key=lambda x: float('-inf') if x is None else x.val)

            # Make the corresponding calls to each child for both graphs
            left_valid = check_flip_equivs(graph_1_order[0], graph_2_order[0])
            right_valid = check_flip_equivs(graph_1_order[1], graph_2_order[1])
            return left_valid and right_valid

        return check_flip_equivs(root1, root2)
# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # root_1 = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8]
    # root_2 = [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]
    # solution_instance = Solution()
    # solution_to_return = solution_instance.flipEquiv(root_1, root_2)
    # print(solution_to_return)
    test_var = sorted([None, 1, 3, 5, 2, None], key = lambda x: float('-inf') if x is None else x)
    print(test_var)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# [1,2,3,4,5,6,null,null,null,7,8]
# [1,3,2,null,6,4,5,null,null,null,null,8,7]

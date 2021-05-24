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
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # Kick off the process by calling traverse
        return self.traverse(s, t)
        """
        Helper function that pre-order traverses each node of the tree recursively.
        Returns true if there is some subtree of s that matches t,
        otherwise returns false.

        Stops when the current node being examined for s is null.
        """

    def traverse(self, s: TreeNode, t: TreeNode) -> bool:
        # Base Case:
        if s is None:
            return False
        # Check if the current subtree is equal to t
        if self.checkEquality(s, t):
            return True
        # Recursively traverse the left subtree first
        if self.traverse(s.left, t):
            return True
        # Recursively traverse the right subtree
        if self.traverse(s.right, t):
            return True
        # If none of these were true, that means no subtree was found
        return False
    """
    Recursive function to check that each node in s and t match
    """
    def checkEquality(self, s: TreeNode, t: TreeNode) -> bool:
        # If we are at the end of the tree, past a leaf
        if s is None and t is None:
            return True
        # If only one of the s and t is None, then they are unequal.
        if s is None or t is None:
            return False
        # We only need to check the left and right subtrees for equality if the current nodes are equal
        if s.val == t.val:
            # Check if the left and right subtrees are equal, recursively
            if self.checkEquality(s.left, t.left) and self.checkEquality(s.right, t.right):
                return True
            else:
                return False
        # If the current nodes weren't equal, return false
        else:
            return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    s = createBTree([3,4,5,1,2], 0)
    t = createBTree([4,1,2], 0)
    solution_instance = Solution()
    solution_to_return = solution_instance.isSubtree(s, t)
    print(solution_to_return)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

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


class Solution(object):
    # Memoization dictionary
    memoization = {1: [TreeNode()],
                   3: [TreeNode(0, TreeNode(0), TreeNode(0))]}
    def allPossibleFBT(self, N):
        if N % 2 == 0:
            return []  # This should never happen
        # Base Case/if has already been computed
        if N in self.memoization:
            return self.memoization[N]
        # Create all possible different subtrees
        answers = []
        for i in range(1, N, 2):  # Increment by 2 so that we only have odd numbers from 1 to N (not including N)
            left_subtree = self.allPossibleFBT(i)
            right_subtree = self.allPossibleFBT(N - i - 1)
            for left in left_subtree:
                for right in right_subtree:
                    new_root = TreeNode()
                    new_root.left = left
                    new_root.right = right
                    answers.append(new_root)
        self.memoization[N] = answers
        return self.memoization[N]


# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     solution_instance = Solution()
#     solution_to_return = solution_instance.allPossibleFBT(7)
#     print(solution_to_return)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

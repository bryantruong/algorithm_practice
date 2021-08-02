# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
My approach will be a BFS approach, using a deque.
How will we know how many are at each level? Use two loops
The first loop will be the while loop (while things are still on the queue)
The second loop will process each level
At each level, create a list for the level. After the inner loop, append the level list to the final list.
Append each node to a list.


Example:

node_queue = [3]
The size of the queue is one, so we only run inner loop once.
pop_left(), so current_node is 3. Add 3 to final list node_queue is now empty: []
Add each of it's children to the queue: 9 and 20. node_queue = [9, 20]

The size of the queue is now two. (run the inner loop to process each node twice)
pop_left for 9, so node_queue is now [20]. Add 9 to final list
9 doesn't have any children.
pop_left for 20, so node_queue is now empty: [] Add 20 too the fiinal list
Add each of its children to the node_queue: [15, 7]

The size of the queue is now two. Run the inner loop 2x to process each node in the queue.
pop_left for 15, no children.
pop_left for 7, no children

Nothing on the queue, end.

Time Complexity: O(N), where N is the number of nodes. Space complexity: O(N)
"""
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        node_queue = deque()
        if not root:
            return []
        node_queue.append(root)
        final_list = []
        while node_queue:
            level_list = []
            for _ in range(len(node_queue)):
                curr_node = node_queue.popleft()
                level_list.append(curr_node.val)
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            final_list.append(level_list)
        return final_list

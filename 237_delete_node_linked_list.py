class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        Replaces contents of current node with next node
        and erases the next node from memory. Can't actually "delete it" and unlink the current node,
        since we don't have access to the previous node.
        """

        node_to_cleanup = node.next
        node.val = node.next.val
        node.next = node.next.next
        # Use del to make sure that the memory is cleared up (prevent memory leak)
        # This is better than setting to None, since we won't be referencing the variable again
        del node_to_cleanup

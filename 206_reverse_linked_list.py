class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def createLinkedList(node_list, cycle_index_pos):
    """
    :param node_list: List of nodes to be put into list
    :param cycle_index_pos: The index that the last node in node_list should point to, creating a cycle.
    :return:
    """

    def search_by_index(head, index):
        current_node = head
        for i in range(index):
            current_node = current_node.next
        return current_node

    # Function to insert node
    def insert(root, item, items_next=None):
        # This will only get used if this is going to be the head
        new_node = ListNode(item)
        if items_next:
            node_to_link_to = search_by_index(root, items_next)
            new_node.next = node_to_link_to
        if not root:
            root = new_node
        else:
            # We have to iterate through to the end of the list
            current = root
            while current.next:
                current = current.next
            current.next = new_node
        return root

    root = None
    for i in range(len(node_list)):
        if i == (len(node_list) - 1):
            root = insert(root, node_list[i], cycle_index_pos)
        else:
            root = insert(root, node_list[i])
    return root


class Solution:
    def reverseList(self, head):
        current_node = head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return prev_node


if __name__ == '__main__':
    solutionObject = Solution()
    linked_list_head = createLinkedList([3, 2, 0, -4], None)
    print("Linked list created")
    reversed_head = solutionObject.reverseList(linked_list_head)
    print("Reversed!")
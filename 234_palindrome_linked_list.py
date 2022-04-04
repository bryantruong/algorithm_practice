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
    def isPalindrome(self, head):
        first_half_end = self.get_first_half_end(head)
        reversed_second_half = self.get_reversed_second_half(first_half_end.next)
        return self.check_palindrome(head, reversed_second_half)

    def get_first_half_end(self, start_node):
        slow = start_node
        fast = start_node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def get_reversed_second_half(self, start_node):
        # This is a standard reversed linked list function
        current_node = start_node
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return prev_node

    def check_palindrome(self, first_half_node, second_half_node):
        while second_half_node:
            if first_half_node.val != second_half_node.val:
                return False
            first_half_node = first_half_node.next
            second_half_node = second_half_node.next
        return True


if __name__ == '__main__':
    solutionObject = Solution()
    linked_list_head = createLinkedList([1, 2, 2, 1], None)
    print(solutionObject.isPalindrome(linked_list_head))
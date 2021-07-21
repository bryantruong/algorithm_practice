# Definition for singly-linked list.
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
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        mid_left = self.get_mid(head)
        # Set the right side before it gets reassigned
        right = mid_left.next
        # Make sure the left half of the list terminates
        mid_left.next = None
        # I don't think that we actually need to set the sorted versions to any variable, since objects passed by ref
        left = self.sortList(head)
        right = self.sortList(right)
        return self.merge_routine(left, right)

    def get_mid(self, list_head):
        # Returns the middle element, which will be the new start of the second half of the list
        # In the case of the length of the list being even, it is conservative (like integer division, rounds down)
        slow, fast = list_head, list_head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_routine(self, left, right):
        current_node = dummy_head = ListNode(None)
        while left and right:
            if left.val < right.val:
                current_node.next = ListNode(left.val)
                left = left.next
            else:
                current_node.next = ListNode(right.val)
                right = right.next
            current_node = current_node.next
        # One of the lists is now empty, so append the rest of the non-empty one (if one exists)
        if left:
            current_node.next = left
        if right:
            current_node.next = right
        return dummy_head.next


if __name__ == '__main__':
    solutionObject = Solution()
    linked_list_head = createLinkedList([1, 3, 2], None)
    sorted_list = solutionObject.sortList(linked_list_head)
    print("Done")

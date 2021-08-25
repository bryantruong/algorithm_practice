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
    """
    We are given the heads of two lists that represent numbers.
    Digits are stored in reverse order, with each node containing a single digit.
    Return the sum of the two numbers as a linked list (also in reverse order)
    Ex:
    2 -> 4 -> 3
    5 -> 6 -> 4
    Returns 807 (the sum of 342 + 465) in the form of 7 -> 0 -> 8

    Ex 2:
    9 -> 9 -> 9 -> 9 -> 9 -> 9 -> 9
    9 -> 9 -> 9 -> 9

    9,999,999 + 9,999 = 10,009,998  in the form of  8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 0

    Solution: Iterate through each linked list, creating a string (being careful of the reverse order).
    Convert each string to int and add.
    Once we have the int, convert to string, and make the new linked list via dummy head node.
    """

    def addTwoNumbers(self, l1, l2):
        first_number = ""
        curr_l1 = l1
        # Get the first value
        while curr_l1:
            first_number = str(curr_l1.val) + first_number
            curr_l1 = curr_l1.next
        # Get the second value
        second_number = ""
        curr_l2 = l2
        while curr_l2:
            second_number = str(curr_l2.val) + second_number
            curr_l2 = curr_l2.next
        # Convert them to integers
        first_number = int(first_number)
        second_number = int(second_number)
        solution_num = str(first_number + second_number)
        # We can let it default to its standard values
        dummy_head = ListNode(float('-inf'))
        dummy_pointer = dummy_head
        for index in range(len(solution_num) - 1, -1, -1):
            curr_digit = solution_num[index]
            curr_node = ListNode(int(curr_digit))
            dummy_pointer.next = curr_node
            dummy_pointer = dummy_pointer.next
        return dummy_head.next



if __name__ == '__main__':
    solutionObject = Solution()
    l1 = createLinkedList([2, 4, 3], None)
    l2 = createLinkedList([5, 6, 4], None)
    print(solutionObject.addTwoNumbers(l1, l2))

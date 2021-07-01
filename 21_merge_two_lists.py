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


def printLinkedList(head):
    """
    :param head: Node that is the head of list.
    :return: void, only prints
    """
    output_string = ""
    while True:
        output_string += str(head.val)
        if not head.next:
            break
        else:
            output_string += "->"
            head = head.next
    print(output_string)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        # no point in assigning a value for the dummy head
        dummy_head = ListNode(None)
        # Repeat this process
        curr_node = dummy_head
        while l1 or l2:
            if l1 is None:
                curr_node.next = l2
                return dummy_head.next
            if l2 is None:
                curr_node.next = l1
                return dummy_head.next
            if l1.val <= l2.val:
                # In the case of a tie, l1 gets priority
                curr_node.next = l1
                # Advance l1
                l1 = l1.next
            else:
                # In the case that l2 is less than l1
                curr_node.next = l2
                l2 = l2.next
            curr_node = curr_node.next
        return "I didn't think we'd get here!"

    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     ############################################################
    #     # My solution actually sucks. Somehow I way overthought it...
    #     # Just google to find an actually good solution. Mine has same time complexity though.
    #     ############################################################
    #     # Rare Cases
    #     if not l1 and not l2:
    #         return None
    #     if not l1:
    #         return l2
    #     if not l2:
    #         return l1
    #
    #     # First determine which list will be the node that we start with (and add other list into)
    #     if l1.val <= l2.val:
    #         main = l1
    #         to_add = l2
    #     else:
    #         main = l2
    #         to_add = l1
    #     # Save off the head of the main list to return
    #     main_head = main
    #     # Save off the next node in main, since we'll need it to reconnect the incoming merged section
    #     main_next = main.next
    #
    #     # Begin iterating through the lists. Can stop once the second list (to_add list) is merged fully merged in
    #     while to_add:
    #         # When the main list has been iterated through, and we just need to append to_add to it
    #         if main_next is None:
    #             main.next = to_add
    #             # Break out of the while loop
    #             to_add = None
    #         # Check if the current value does not fit between the interval. If not, move the main pointers.
    #         elif to_add.val > main_next.val:  # We already know that it is greater than or equal to main_next
    #             # Move on to the next pointers for main
    #             main = main_next
    #             main_next = main_next.next
    #         else:
    #             # Need to save the current node, as well as the starting node of the to_add chain
    #             curr_to_add = to_add
    #             while curr_to_add.next:
    #                 # At this point, if we are in this "else" block, we already know that to_add's value is valid.
    #                 if curr_to_add.next.val <= main_next.val:
    #                     # Move to the next node
    #                     curr_to_add = curr_to_add.next
    #                 else:
    #                     break
    #             # Rewire
    #             main.next = to_add
    #             to_add = curr_to_add.next
    #             curr_to_add.next = main_next
    #
    #             # Advance the pointer for the next iteration of the outer loop
    #             main = main_next
    #             main_next = main_next.next
    #
    #         # First check to see if the to_add value is within the interval.
    #     return main_head


if __name__ == '__main__':
    solutionObject = Solution()
    l1 = createLinkedList([1, 2, 4], None)
    l2 = createLinkedList([1, 3, 4], None)
    solution_node = solutionObject.mergeTwoLists(l1, l2)
    printLinkedList(solution_node)

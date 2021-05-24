# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Helper function to create the linked list head
def createLinkedList(node_list, cycle_index_pos):
    def search_by_index(head, index):
        current_node = head
        for i in range(index):
            current_node = current_node.next
        return current_node


    # Function to insert node
    def insert(root, item, items_next = None):
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
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        if not head:
            return False
        while head.next:
            curr_len = len(visited)
            visited.add(head)
            if curr_len == len(visited):
                return True
            head = head.next
        return False



if __name__ == '__main__':
    solutionObject = Solution()
    linked_list_head = createLinkedList([3,2,0,-4], 1)
    print(solutionObject.hasCycle(linked_list_head))
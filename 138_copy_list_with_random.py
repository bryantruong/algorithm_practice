"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# I am not going to bother to try to make the function to actually make the linked list

class Solution:
    # This is the recursive solution. I looked at the solution for this. My original solution is commented below itÒ
    def __init__(self):
        self.mappings = {None: None}

    def copyRandomList(self, head: 'Node') -> 'Node':
        def recursive_search(original_node):
            if not head:
                return None
            if head in self.mappings:
                return self.mappings[head]
            else:
                # Put it in the mappings, as we have seen it
                new_node = Node(head.val, None, None)
                # It is important to add it to the dictionary now. Later calls will use it to set next and random
                self.mappings[head] = new_node
                new_node.next = self.copyRandomList(head.next)
                new_node.random = self.copyRandomList(head.random)

                return new_node
        recursive_search(head)
        return self.mappings[head]

    # def copyRandomList(self, head: 'Node') -> 'Node':
    #     # Corner Case
    #     if not head:
    #         return None
    #     dummy_head = Node(-10000, None, None)
    #     current_original = head
    #     current_copy = dummy_head
    #     # Will map the old node to the new node object
    #     mappings = {None: None}
    #     # Current original will always be one ahead of current_copy
    #     # First iterate through to copy the simple linked list. Will add the randoms in a second while loop
    #     while current_original:
    #         if current_original not in mappings:
    #             # We will update the random part in a second while loop
    #             copy_of_original = Node(current_original.val, None, current_original.random)
    #             mappings[current_original] = copy_of_original
    #         current_copy.next = mappings[current_original]
    #         # Set the current original to the original list's next
    #         current_original = current_original.next
    #         # Set the current copy to the next node in the new list
    #         current_copy = current_copy.next
    #     # Iterate through again, to update/fix the randoms
    #     current_copy = dummy_head.next
    #     while current_copy:
    #         current_copy.random = mappings[current_copy.random]
    #         current_copy = current_copy.next
    #     return dummy_head.next


if __name__ == '__main__':
    # I will not be testing it on here, since there is the added field for random
    print("Submit to LC to test")

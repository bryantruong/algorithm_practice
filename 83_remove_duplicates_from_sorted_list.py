# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        dummy_head = ListNode(val=-101, next=head)
        prev = dummy_head
        curr = head
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next  # Remove reference to current, since it is a duplicate
            else:
                prev = prev.next  # Otherwise, advance the previous pointer
            curr = curr.next  # Always advance the curr pointer. If it is another duplicate, it gets addressed next iter
        return dummy_head.next

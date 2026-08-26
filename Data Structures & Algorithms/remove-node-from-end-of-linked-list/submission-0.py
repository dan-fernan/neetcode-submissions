# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        remIdx = length - n - 1

        dh = ListNode(0)
        dh.next = head
        curr = dh
        pos = -1

        while pos < remIdx:
            curr = curr.next
            pos += 1
        curr.next = curr.next.next

        return dh.next
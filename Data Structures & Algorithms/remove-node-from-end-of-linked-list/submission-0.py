# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        while fast:
            fast = fast.next
            if n + 1 > 0:
                n -= 1
                continue
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
                


        
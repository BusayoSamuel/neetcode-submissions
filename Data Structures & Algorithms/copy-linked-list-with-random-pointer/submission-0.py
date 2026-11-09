"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        dummy = Node(0, head)
        cur = dummy.next

        while cur:
            hashmap[cur] = Node(cur.val)
            cur = cur.next

        hashmap[cur] = None

        cur = dummy.next

        while cur:
            hashmap[cur].next = hashmap[cur.next]
            hashmap[cur].random = hashmap[cur.random]
            cur = cur.next

        return hashmap[dummy.next]
        
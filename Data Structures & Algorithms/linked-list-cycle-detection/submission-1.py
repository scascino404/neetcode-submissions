# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head
        while tortoise and hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise is hare:
                return True
        return False
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        node1 = list1
        node2 = list2
        while node1 and node2:
            if node1.val <= node2.val:
                current.next = node1
                node1 = node1.next
            else:
                current.next = node2
                node2 = node2.next
            current = current.next
        if node1:
            current.next = node1
        elif node2:
            current.next = node2
        return dummy.next
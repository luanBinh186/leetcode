# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_num = 0
        l3 = ListNode(0)
        current = l3
        while l1 is not None or l2 is not None or carry_num != 0:
            sum = (0 if (l1 is None) else l1.val) + (0 if (l2 is None) else l2.val) + carry_num
            carry_num = sum // 10
            sum = sum % 10
            current.next = ListNode(sum)
            current = current.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return l3.next
        
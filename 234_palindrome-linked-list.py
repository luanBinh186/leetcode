# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        second_half = self.reverse_linked_list(slow)

        # Compare the reversed second half with the first half
        while second_half is not None:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        return True

    def reverse_linked_list(self, head):
        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
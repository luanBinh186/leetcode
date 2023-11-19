from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#
#
# def isPalindrome(head: Optional[ListNode]) -> bool:
#     return True


def is_palindrome(head: Optional[ListNode]):
    # Find the middle using Fast & Slow Pointers
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    second_half = reverse_linked_list(slow)

    # Compare the reversed second half with the first half
    while second_half is not None:
        if head.val != second_half.val:
            return False
        head = head.next
        second_half = second_half.next
    return True

def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


if __name__ == '__main__':
    # Example usage
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)

    result = is_palindrome(head)
    print(result)  # Output: True



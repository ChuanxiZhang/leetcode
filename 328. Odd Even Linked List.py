# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head:
            odd.next = head
            odd = odd.next
            even.next = head.next
            even = even.next
            head = head.next.next if even else None

        odd.next = dummy2.next

        return dummy1.next

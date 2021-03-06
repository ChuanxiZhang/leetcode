# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        if not head:
            return head
        prev = None
        curr = head
        while curr:
           next=curr.next
           curr.next= prev
           prev= curr
           curr = next
        return prev
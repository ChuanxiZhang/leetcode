# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        def reverse(node):
            prev = None
            curr = node
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        a=ra = reverse(headA)
        b=rb = reverse(headB)
        pos = None
        while ra and rb and ra.val == rb.val:
            pos = ra
            print pos
            ra = ra.next
            rb = rb.next
        headA=reverse(a)
        headB=reverse(b)
        return pos
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
          
        p = head
        s = 1
        while p.next != None:
            p = p.next
            s += 1

        if s == 1 and n == 1:
            head.next = None
            head = head.next
            return head

        r = s - n 
        if r == 0:
            head = head.next
            return head

        p = head
        t = head
        for i in range(0,r+1):
            if i != r:
                t = p
                p = p.next
            else:
                print(i)
                t.next = p.next
        return head
        
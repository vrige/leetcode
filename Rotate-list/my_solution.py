# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 0:
            return head

        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        k = k % count

        for time in range(k):
            temp = head

            bring_f = []
            while temp:
                bring_f.append(temp.val)
                if temp and len(bring_f) > 1:
                    temp.val = bring_f.pop(0)
                temp = temp.next
                
            head.val = bring_f.pop(0)
            
        return head
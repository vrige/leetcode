# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head:

            origin = head
            swap = True
            prev = None

            while head != None:
                
                if swap:
                    prev = head
                    swap = False
                    head = head.next

                else:
                    c = head.val
                    head.val = prev.val
                    prev.val = c
                    swap = True
                    head = head.next
            
            return origin
        else:           
            return None
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        out = ListNode()
        origin = out

        if list1 == None and list2 == None:
            out.next = None
            out = None
            return out
        
        while list1 != None or list2 != None:

            valN = None

            if list1 == None:
                valN = list2.val
                list2 = list2.next
            elif list2 == None:
                valN = list1.val
                list1 = list1.next
            else: 
                if list1.val <= list2.val:
                    valN = list1.val
                    list1 = list1.next
                else:
                    valN = list2.val
                    list2 = list2.next
            
            out.val = valN

            if list1 != None or list2 != None:
                out.next = ListNode()
                out = out.next
            else:
                out = None

        return origin
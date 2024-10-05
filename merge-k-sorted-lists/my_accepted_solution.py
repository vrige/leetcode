# Definition for singly-linked list.

class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):    
            self.val = val
            self.next = next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        n = len(lists)
        out = ListNode(float("-inf"))
        b = out
        c = b

        if n == 1:
            return lists[0]
        if n == 0:
            return ListNode().next

        while True:
            minn = float('inf')
            min_ind = -1
            empty = 0

            for i in range(n):
                if lists[i] == None:
                    empty += 1
                    continue
                   
                if minn > lists[i].val:
                    minn = lists[i].val
                    min_ind = i


            if minn == float('inf'):
                if empty == n and c.val == float("-inf"):
                    return ListNode().next
                c.next = None
                break

            a = lists[min_ind].val
            lists[min_ind]= lists[min_ind].next
            
            b.val = a
            b.next = ListNode()
            c = b
            b = b.next

        return out


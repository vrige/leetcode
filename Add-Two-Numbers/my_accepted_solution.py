# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    counter = 0
    NodeList = []
    adding = 0

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.cleanUp()
        return self.addTwoNumers_(l1,l2)

    def addTwoNumers_(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # check value constraints
        if l1.val <= 9 and l1.val >= 0 and l2.val <= 9 and l2.val >= 0 and self.counter <= 100:
            
            self.counter += 1
            l3_val = l1.val + l2.val + self.adding
            self.adding = 0

            if l3_val > 9:
                l3_val = l3_val % 10
                self.adding += 1

            self.NodeList.append(ListNode(l3_val))

            if l1.next != None and l2.next != None:
                return self.addTwoNumers_(l1.next, l2.next)
            elif l1.next != None:
                return self.reportSingleNumer(l1.next)
            elif l2.next != None:
                return self.reportSingleNumer(l2.next)
            elif self.adding != 0:
                self.NodeList.append(ListNode(self.adding))
                return self.assembleNodeList()
            else:
                return self.assembleNodeList()
    
    def reportSingleNumer(self, l1: Optional[ListNode]) -> Optional[ListNode]:

        if l1.val <= 9 and l1.val >= 0 and self.counter <= 100:
            
            self.counter += 1
            l3_val = l1.val + self.adding
            self.adding = 0

            if l3_val > 9:
                l3_val = l3_val % 10
                self.adding += 1

            self.NodeList.append(ListNode(l3_val))

            if l1.next != None:
                return self.reportSingleNumer(l1.next)
            elif self.adding != 0:
                self.NodeList.append(ListNode(self.adding))
                return self.assembleNodeList()
            else:
                return self.assembleNodeList()

    def assembleNodeList(self) -> Optional[ListNode]:

        for count, value in enumerate(self.NodeList):

            if count + 1 < len(self.NodeList):
                value.next = self.NodeList[count + 1]
        
        return self.NodeList[0]

    def cleanUp(self):
        self.NodeList = []
        self.counter = 0
        self.adding = 0
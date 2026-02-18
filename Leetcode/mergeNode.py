from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        listNode = None
        head = None
        temp1 = list1
        temp2 = list2
        while temp1 != None and temp2 != None:
            if temp1.val <= temp2.val:
                newNode =  ListNode(temp1.val)
                if head == None:
                    listNode = newNode
                    head = newNode
                else:
                    head.next = newNode
                    head = newNode
                temp1 = temp1.next
            elif temp2.val < temp1.val:
                newNode =  ListNode(temp2.val)
                if head == None:
                    listNode = newNode
                    head = newNode
                else:
                    head.next = newNode
                    head = newNode
                temp2 = temp2.next
        while temp1 != None:
            newNode =  ListNode(temp1.val)
            if head == None:
                head = newNode
            else:
                head.next = newNode
            head = newNode
            temp1 = temp1.next
        while temp2 != None:
            newNode =  ListNode(temp2.val)
            if head == None:
                head = newNode
            else:
                head.next = newNode
            head = newNode
            temp2 = temp2.next
        return listNode

list1 = ListNode()
list2 = ListNode(0)

sol = Solution()
print(sol.mergeTwoLists(list1,list2))
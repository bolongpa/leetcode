# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1)
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            if l1.val <= l2.val:
                L1 = l1
                L2 = l2
            else:
                L1 = l2
                L2 = l1
            head = L1

            if L1.next == None:
                L1.next = L2
            else:
                while L1.next != None:
                    while L2 != None:
                        if L1.val <= L2.val < L1.next.val:
                            temp = L2
                            L2 = L2.next
                            temp.next = L1.next
                            L1.next = temp
                            L1 = L1.next
                        else:
                            break
                    L1 = L1.next
                if L2 != None:
                    L1.next = L2

            return head

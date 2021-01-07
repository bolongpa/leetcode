# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from copy import deepcopy


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:  # empty list
            return head
        else:
            res = ListNode()
            output = res
            n1 = head
            n2 = head.next
            while n1:
                if n2:
                    res.next = deepcopy(n2)
                    res = res.next
                    res.next = deepcopy(n1)
                    res = res.next
                    res.next = None

                    n1 = n2.next
                    if n1:
                        n2 = n1.next
                else:
                    res.next = deepcopy(n1)
                    n1 = n1.next
            return output.next

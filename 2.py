# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        head = res
        r = False  # regrouping initialized with false
        while l1 or l2:
            if l1 is None:  # l2 is not None
                if not r:  # r is False, no regrouping
                    res.next = l2
                    res = res.next
                    l2 = l2.next
                else:  # r is True
                    l2.val += 1
                    if l2.val > 9:
                        l2.val = 0
                        r = True
                        res.next = l2
                        res = res.next
                        l2 = l2.next
                    else:
                        r = False
                        res.next = l2
                        res = res.next
                        l2 = l2.next

            elif l2 is None:
                if not r:  # r is False, no regrouping
                    res.next = l1
                    res = res.next
                    l1 = l1.next
                else:  # r is True
                    l1.val += 1
                    if l1.val > 9:
                        l1.val = 0
                        r = True
                        res.next = l1
                        res = res.next
                        l1 = l1.next
                    else:
                        r = False
                        res.next = l1
                        res = res.next
                        l1 = l1.next

            else:  # l1 and l2 both not none
                if not r:  # no regrouping
                    sumdigit = l1.val + l2.val
                else:
                    sumdigit = l1.val + l2.val + 1
                if sumdigit > 9:
                    sumdigit = sumdigit % 10
                    r = True
                else:
                    r = False
                new_node = ListNode()
                new_node.val = sumdigit
                res.next = new_node
                res = res.next
                l1 = l1.next
                l2 = l2.next

        # final check r if need regrouping
        if r:
            last = ListNode()
            last.val = 1
            res.next = last
        return head.next


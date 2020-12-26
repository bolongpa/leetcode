"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root != None:
            depth = 1
            pivot = root
            children = pivot.children
            while children != []:
                print(children)
                temp = []
                for c in children:
                    temp.extend(c.children)
                children = temp
                depth += 1
            return depth
        else:
            return 0

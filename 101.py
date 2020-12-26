# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # BFS
        # root == None
        if not root:
            return True
        else:
            lvl = [root]
            while not all([i == None for i in lvl]):
                next_lvl = []
                for n in lvl:
                    if n.left:
                        next_lvl.append(n.left)
                    else:
                        next_lvl.append(None)
                    if n.right:
                        next_lvl.append(n.right)
                    else:
                        next_lvl.append(None)
                next_lvl_val = [n.val if n else None for n in next_lvl]
                # check if symmetric
                if next_lvl_val != next_lvl_val[::-1]:
                    return False
                lvl = [n for n in next_lvl if n]
            return True
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.ls = []
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return

        self.ls.append(root.val)
        for item in root.children:
            self.preorder(item)

        return self.ls
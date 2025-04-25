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
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        for child in root.children:
            self.postorder(child)
        self.ls.append(root.val)
        return self.ls

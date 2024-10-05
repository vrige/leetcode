# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_ = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_ = 0

        def sea(ver, ind):

            #left
            if not ver.left is None:
                sea(ver.left, ind +1 )

            #right
            if not ver.right is None:
                sea(ver.right, ind +1)

            if ver.right is None and ver.left is None and self.max_ < ind:
                self.max_ = ind

        if not root is None:
            sea(root, 1)
        
        return self.max_
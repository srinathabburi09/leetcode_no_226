# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:   #this solves the base case
            return None  #so we return None because there is no root or note
        root.left, root.right = root.right, root.left   #if we find a root then root.left = left node of the root and root.right = right node of the root we swap them
        self.invertTree(root.left) #from here root.left will be the main root of the left sub tree thereby it continues as a recursive function
        self.invertTree(root.right) #from here root.right will be the main root of the right sub tree thereby it continues as a recursive function. so the function continues swapping the both nodes
        return root

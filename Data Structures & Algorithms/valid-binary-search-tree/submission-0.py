# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        def isValid(root,lower,upper):
            if(root is None):
                return True
            if(not(lower<root.val<upper)):
                return False
            else:
                return(isValid(root.left,lower,root.val)) and           isValid(root.right,root.val,upper)

        return isValid(root,float("-inf"),float("inf"))

        
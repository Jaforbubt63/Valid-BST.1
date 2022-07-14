# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inorder(node):
            nonlocal last_value
            
            if node is None:
                return True
            
            valid = inorder(node.left)
            if valid is False:
                return False
            
            if node.val <= last_value:
                return False
            
            last_value = node.val
            
            return inorder(node.right)
        
        last_value = -1 * pow(2, 32)
        
        valid = inorder(root)
        return valid
                
        
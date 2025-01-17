# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            
            print(preorder, inorder)
            ele = preorder.pop(0)
           
            ind = inorder.index(ele)
            
            root = TreeNode(inorder[ind])
            
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
        
# Time complexity: O(n)
# Space complexity: O(1)
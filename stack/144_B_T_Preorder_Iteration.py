# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            tmp = stack.pop()
            if tmp:
                res.append(tmp.val)
                if tmp.right:
                    stack.append(tmp.right)
                if tmp.left:
                    stack.append(tmp.left)
        return res

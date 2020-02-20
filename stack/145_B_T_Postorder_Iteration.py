# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res_rev = []
        stack = [root]
        while stack:
            tmp =stack.pop()
            if tmp:
                res_rev.append(tmp.val)
                if tmp.left:
                    stack.append(tmp.left)
                if tmp.right:
                    stack.append(tmp.right)
        res = res_rev[::-1]
        return res
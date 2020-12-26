"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 我的做法
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> list:
#         res = []
#         stack = []
#         cur = root
#         while cur:
#             stack.append(cur.val)
#             if cur.right:
#                 stack.append(cur.right)
#             if cur.left:
#                 cur = cur.left
#             elif len(stack) > 0:
#                 cur = stack.pop()
#                 while type(cur) == int:
#                     res.append(cur)
#                     if len(stack) > 0:
#                         cur = stack.pop()
#                     else:
#                         cur = None
#             else:
#                 cur = None
#
#         return res


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        res = []
        stack = [root]
        while len(stack) > 0:
            cur = stack.pop()
            if isinstance(cur, TreeNode):
                stack.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
            elif isinstance(cur, int):
                res.append(cur)
        return res

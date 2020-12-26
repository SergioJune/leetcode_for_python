"""
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,2,3]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[1,2]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
 

进阶：递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归做法
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> list:
#         res = []
#
#         def inner_traver(root):
#             if root:
#                 res.append(root.val)
#                 inner_traver(root.left)
#                 inner_traver(root.right)
#         inner_traver(root)
#         return res


# 非递归做法
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> list:
#         res = []
#         stack = []
#         cur = root
#         while cur:
#             res.append(cur.val)
#             if cur.right:
#                 stack.append(cur.right)
#             if cur.left:
#                 cur = cur.left
#             elif len(stack) > 0:
#                 cur = stack.pop()
#             else:
#                 cur = None
#         return res


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        res = []
        stack = [root]
        while len(stack) > 0:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)

        return res
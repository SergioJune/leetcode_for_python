"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[2,1]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
 

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 递归做法
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> list:
#
#         def inner_traversal(root):
#             if root is None:
#                 return []
#             res = []
#             res += inner_traversal(root.left)
#             res.append(root.val)
#             res += inner_traversal(root.right)
#             return res
#         return inner_traversal(root)


# 手动模拟栈，使用非递归做法，所以使用栈数据结构来做
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        stack = []
        res = []
        cur = root
        while cur:
            stack.append(cur)
            if cur.left:
                cur = cur.left
            else:
                while len(stack) > 0:
                    cur = stack.pop()
                    res.append(cur.val)
                    if cur.right:
                        cur = cur.right
                        break
                else:
                    cur = cur.right

        return res
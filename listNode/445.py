"""
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

 

示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 这道题还可以使用栈来做，但是做法不够我这样好，我这个时间复杂度O(max(m+n)),空间复杂度O(max(m+n))
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.get_sum(l1)
        num2 = self.get_sum(l2)
        sum_num = num1 + num2
        prev = None
        while sum_num != 0:
            node = ListNode(sum_num%10)
            node.next = prev
            prev = node
            sum_num //= 10
        if prev:
            return prev
        return ListNode(sum_num)

    def get_sum(self, head):
        num = 0
        while head:
            num = num * 10 + head.val
            head = head.next
        return num
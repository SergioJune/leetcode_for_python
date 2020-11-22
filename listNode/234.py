"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        # 找到中间节点
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        else:
            if fast is None:
                other_head = slow
            else:
                other_head = slow.next
            prev.next = None
        other_head = self.reverse_node(other_head)

        # 比较两个节点
        first, secode = head, other_head
        while first:
            if first.val != secode.val:
                return False
            first = first.next
            secode = secode.next
        return True

    def reverse_node(self, head: ListNode):
        prev = None
        now = head
        while now:
            next_node = now.next
            now.next = prev
            prev = now
            now = next_node
        return prev


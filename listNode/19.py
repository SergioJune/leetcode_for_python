"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 第一种解法
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         if head is None:
#             return head
#         if head.next is None and n == 1:
#             return None
#         length_node = 1
#         slow_walk = 0
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             slow_walk += 1
#             for i in range(n+1):
#                 fast = fast.next
#                 if fast is None:
#                     break
#                 length_node += 1
#
#         revome_index = length_node - n
#         if revome_index < 0:
#             return head.next
#         elif slow_walk > revome_index:
#             slow_walk = 0
#             slow = head
#         while slow_walk < revome_index:
#             slow = slow.next
#             slow_walk += 1
#         slow.next = slow.next.next
#         return head


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast = head, head
        for i in range(n):  # 快指针先走 n 步
            fast = fast.next
            if fast is None:
                break

        if fast is None:
            return head.next
        while fast.next:  # 同走 m b步，这样就是 n+m=length
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
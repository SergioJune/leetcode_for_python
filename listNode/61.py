"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         if head is None:
#             return None
#         slow, fast, len_node = head, head, 1
#         for i in range(k):
#             if fast.next is None:
#                 has_run = k % len_node
#                 fast = head
#                 for j in range(has_run):
#                     fast = fast.next
#                 break
#             fast = fast.next
#             len_node += 1
#
#         while True:
#             if fast.next is None:
#                 fast.next = head
#                 break
#             slow = slow.next
#             fast = fast.next
#
#         head = slow.next
#         slow.next = None
#         return head


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        slow, fast, len_node = head, head, 1
        while True:  # 找出链表的长度
            if fast.next is None:
                fast.next = head  # 搞成闭环
                break
            fast = fast.next
            len_node += 1

        run = len_node - (k % len_node) - 1
        for i in range(run):  # 找到头指针的前一个指针
            slow = slow.next

        head = slow.next
        slow.next = None
        return head

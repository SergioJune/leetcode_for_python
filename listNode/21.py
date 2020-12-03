"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        faker1 = ListNode(None, l1)
        faker2 = ListNode(None, l2)
        left, right = faker1, faker2
        while left.next and right.next:
            if left.next.val > right.next.val:
                cur = right.next
                right.next = cur.next
                cur.next = left.next
                left.next = cur

            left = left.next
        if left.next is None:
            left.next = right.next

        return faker1.next

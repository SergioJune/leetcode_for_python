"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        num = 1
        faker = ListNode(None, head)
        cur = faker
        while num < m:
            cur = cur.next
            num += 1

        cur.next = self.reverse(cur.next, n - m + 1)
        return faker.next

    def reverse(self, head, n):
        num = 0
        prev = None
        cur = head
        while cur and num < n:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            num += 1

        head.next = next_node

        return prev
